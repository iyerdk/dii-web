// ── Chat panel ────────────────────────────────────────────────────────────────

function openChat(btn, sectionContext) {
  const card = btn.closest('.research-card');
  const panel = card.querySelector('.chat-panel');
  panel.classList.toggle('hidden');
  if (!panel.classList.contains('hidden')) {
    panel.querySelector('.chat-input').focus();
    // Store context on the panel for use in sendChat
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
