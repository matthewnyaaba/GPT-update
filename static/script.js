
async function sendPrompt() {
    const input = document.getElementById("promptInput");
    const message = input.value.trim();
    if (!message) return;
    addMessage(message, "user");
    input.value = "";
    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });
    const data = await response.json();
    addMessage(data.reply, "bot");
    speakText(data.reply);
}

function addMessage(text, role) {
    const container = document.getElementById("chatContainer");
    const div = document.createElement("div");
    div.className = "message " + role;
    div.textContent = text;
    container.appendChild(div);
    container.scrollTop = container.scrollHeight;
}

function speakText(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(utterance);
}

function startListening() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;
    recognition.start();
    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        document.getElementById("promptInput").value = transcript;
        sendPrompt();
    };
    recognition.onerror = function(event) {
        alert("Speech recognition error: " + event.error);
    };
}
