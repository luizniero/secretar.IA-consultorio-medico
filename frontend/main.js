const messagesDiv = document.getElementById('messages');
const form = document.getElementById('message-form');
const input = document.getElementById('user-input');

const ws = new WebSocket('ws://localhost:8765');

ws.onopen = () => {
    appendMessage('Sistema', 'Aguarde enquanto eu sou conectado...');
};

ws.onmessage = (event) => {
    const data = event.data;
    appendMessage('Agente', data);
};

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const text = input.value;
    if (text) {
        appendMessage('Você', text);
        ws.send(text);
        input.value = '';
    }
});

function appendMessage(sender, text) {
    const msg = document.createElement('div');
    msg.classList.add('message');
    msg.innerHTML = `<strong>${sender}:</strong> ${text}`;
    messagesDiv.appendChild(msg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}
