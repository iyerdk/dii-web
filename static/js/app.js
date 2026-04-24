// ── Text-to-Speech (browser Web Speech API) ───────────────────────────────────
// Chrome fix: speak sentence-by-sentence to avoid the ~15s silent cancellation bug.
// Safari fix: wait for voiceschanged before first speak().

let ttsChunks = [];
let ttsIndex = 0;
let ttsSpeaking = false;
let ttsPaused = false;

function buildTTSChunks() {
  const scriptEl = document.querySelector('.script-content');
  if (!scriptEl) return [];
  let text = scriptEl.innerText || scriptEl.textContent || '';
  // Strip markdown symbols so they aren't read aloud
  text = text.replace(/#{1,3}\s*/g, '').replace(/\*\*/g, '').replace(/\*/g, '').trim();
  // Split into sentences (~100 chars max per chunk to stay well under Chrome's limit)
  return text.match(/[^.!?\n]+[.!?\n]+/g) || [text];
}

function getVoices() {
  return new Promise(resolve => {
    const v = window.speechSynthesis.getVoices();
    if (v.length) { resolve(v); return; }
    window.speechSynthesis.addEventListener('voiceschanged', () => {
      resolve(window.speechSynthesis.getVoices());
    }, { once: true });
  });
}

function toggleTTS() {
  if (!('speechSynthesis' in window)) {
    alert('Text-to-speech is not supported in this browser. Try Chrome or Edge.');
    return;
  }
  if (ttsPaused) {
    window.speechSynthesis.resume();
    ttsPaused = false;
    setTTSState('playing');
    return;
  }
  if (ttsSpeaking) {
    window.speechSynthesis.pause();
    ttsPaused = true;
    setTTSState('paused');
    return;
  }
  setTTSState('loading');
  startTTS();
}

async function startTTS() {
  window.speechSynthesis.cancel();
  ttsChunks = buildTTSChunks();
  ttsIndex = 0;
  if (!ttsChunks.length) { setTTSState('stopped'); return; }
  await getVoices();
  ttsSpeaking = true;
  ttsPaused = false;
  speakNext();
}

function speakNext() {
  if (!ttsSpeaking || ttsIndex >= ttsChunks.length) {
    ttsSpeaking = false;
    setTTSState('stopped');
    return;
  }
  const utt = new SpeechSynthesisUtterance(ttsChunks[ttsIndex]);
  utt.rate = 0.92;
  utt.lang = 'en-US';
  utt.onstart = () => { if (ttsIndex === 0) setTTSState('playing'); };
  utt.onend = () => { ttsIndex++; speakNext(); };
  utt.onerror = (e) => {
    if (e.error === 'interrupted' || e.error === 'canceled') return;
    ttsSpeaking = false;
    setTTSState('stopped');
  };
  window.speechSynthesis.speak(utt);
  // Ensure visible state after first chunk fires
  if (ttsIndex === 0) setTimeout(() => { if (ttsSpeaking) setTTSState('playing'); }, 300);
}

function stopTTS() {
  ttsSpeaking = false;
  ttsPaused = false;
  window.speechSynthesis.cancel();
  setTTSState('stopped');
}

function setTTSState(state) {
  const btn = document.getElementById('tts-btn');
  const controls = document.getElementById('tts-controls');
  const status = document.getElementById('tts-status');
  if (!btn) return;
  const icon = btn.querySelector('.tts-icon');
  const label = btn.querySelector('.tts-label');

  if (state === 'playing') {
    icon.textContent = '⏸'; label.textContent = 'Pause';
    controls && controls.classList.remove('hidden');
    status && (status.textContent = 'Reading…');
  } else if (state === 'paused') {
    icon.textContent = '▶'; label.textContent = 'Resume';
    status && (status.textContent = 'Paused');
  } else if (state === 'loading') {
    icon.textContent = '…'; label.textContent = 'Starting…';
    controls && controls.classList.add('hidden');
  } else {
    icon.textContent = '▶'; label.textContent = 'Listen';
    controls && controls.classList.add('hidden');
  }
}

window.addEventListener('beforeunload', () => {
  window.speechSynthesis && window.speechSynthesis.cancel();
});

// ── Card expand/collapse ──────────────────────────────────────────────────────

function toggleCard(headerBtn) {
  const card = headerBtn.closest('.research-card');
  const body = card.querySelector('.card-body');
  const expanded = headerBtn.getAttribute('aria-expanded') === 'true';

  headerBtn.setAttribute('aria-expanded', !expanded);
  body.classList.toggle('hidden', expanded);
  card.classList.toggle('expanded', !expanded);
}

// ── Chat panel ────────────────────────────────────────────────────────────────

function openChat(btn, sectionContext) {
  const card = btn.closest('.research-card');
  const panel = card.querySelector('.chat-panel');
  panel.classList.toggle('hidden');
  if (!panel.classList.contains('hidden')) {
    panel.querySelector('.chat-input').focus();
    panel.dataset.context = sectionContext;
    panel.dataset.slug = card.dataset.slug;
  }
}

function sendChat(sendBtn) {
  const panel = sendBtn.closest('.chat-panel');
  const input = panel.querySelector('.chat-input');
  const messages = panel.querySelector('.chat-messages');
  const question = input.value.trim();
  if (!question) return;

  // Add user bubble
  appendMsg(messages, 'user', question);
  input.value = '';

  // Add loading indicator
  const loadingEl = appendMsg(messages, 'loading', 'Thinking…');

  fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      episode_slug: panel.dataset.slug,
      section_context: panel.dataset.context || '',
      question: question,
    }),
  })
    .then(r => r.json())
    .then(data => {
      loadingEl.remove();
      appendMsg(messages, 'assistant', data.answer || data.detail || 'No response.');
    })
    .catch(() => {
      loadingEl.remove();
      appendMsg(messages, 'assistant', 'Error contacting AI. Please try again.');
    });
}

function appendMsg(container, type, text) {
  const el = document.createElement('div');
  el.className = `chat-msg ${type}`;
  el.textContent = text;
  container.appendChild(el);
  container.scrollTop = container.scrollHeight;
  return el;
}

// Allow Enter key in chat input
document.addEventListener('keydown', e => {
  if (e.key === 'Enter' && e.target.classList.contains('chat-input')) {
    const sendBtn = e.target.closest('.chat-input-row').querySelector('.chat-send');
    sendBtn.click();
  }
});
