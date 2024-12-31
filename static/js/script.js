function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    const chatbox = document.getElementById("chatbox");

    if (userInput.trim() === "") return;

    chatbox.innerHTML += `<div><b>Anda:</b> ${userInput}</div>`;
    document.getElementById("userInput").value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput }),
    })
        .then((response) => response.json())
        .then((data) => {
            chatbox.innerHTML += `<div><b>Chatbot:</b> ${data.response}</div>`;
            chatbox.scrollTop = chatbox.scrollHeight;
        });
}
