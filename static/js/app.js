// ── Text-to-Speech (browser Web Speech API) ───────────────────────────────────

let ttsUtterance = null;
let ttsSpeaking = false;

function buildTTSText() {
  // Extract the full script content, splitting MAYA/JAMES lines
  const scriptEl = document.querySelector('.script-content');
  if (!scriptEl) return '';
  // Get text, preserving paragraph breaks
  return scriptEl.innerText || scriptEl.textContent || '';
}

function toggleTTS() {
  if (!('speechSynthesis' in window)) {
    alert('Your browser does not support text-to-speech. Try Chrome or Edge.');
    return;
  }
  if (ttsSpeaking) {
    pauseTTS();
    return;
  }
  if (window.speechSynthesis.paused) {
    window.speechSynthesis.resume();
    setTTSState(true);
    return;
  }
  startTTS();
}

function startTTS() {
  window.speechSynthesis.cancel();
  const text = buildTTSText();
  if (!text) return;

  ttsUtterance = new SpeechSynthesisUtterance(text);
  ttsUtterance.rate = 0.95;
  ttsUtterance.pitch = 1;
  ttsUtterance.lang = 'en-US';

  ttsUtterance.onstart = () => setTTSState(true);
  ttsUtterance.onend = () => setTTSState(false);
  ttsUtterance.onerror = () => setTTSState(false);

  window.speechSynthesis.speak(ttsUtterance);
}

function pauseTTS() {
  if (window.speechSynthesis.speaking) {
    window.speechSynthesis.pause();
    setTTSState(false, true);
  }
}

function stopTTS() {
  window.speechSynthesis.cancel();
  setTTSState(false);
}

function setTTSState(playing, paused) {
  ttsSpeaking = playing;
  const btn = document.getElementById('tts-btn');
  const controls = document.getElementById('tts-controls');
  const status = document.getElementById('tts-status');
  if (!btn) return;

  if (playing) {
    btn.querySelector('.tts-icon').textContent = '⏸';
    btn.querySelector('.tts-label').textContent = 'Pause';
    controls && controls.classList.remove('hidden');
    status && (status.textContent = 'Reading…');
  } else if (paused) {
    btn.querySelector('.tts-icon').textContent = '▶';
    btn.querySelector('.tts-label').textContent = 'Resume';
    status && (status.textContent = 'Paused');
  } else {
    btn.querySelector('.tts-icon').textContent = '▶';
    btn.querySelector('.tts-label').textContent = 'Listen';
    controls && controls.classList.add('hidden');
  }
}

// Stop TTS when navigating away
window.addEventListener('beforeunload', () => window.speechSynthesis && window.speechSynthesis.cancel());

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
