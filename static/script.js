
async function sendPrompt() {
    const prompt = document.getElementById('promptInput').value;
    const responseBox = document.getElementById('responseBox');
    responseBox.innerText = "Thinking...";
    const res = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: prompt })
    });
    const data = await res.json();
    responseBox.innerText = data.reply;
}
