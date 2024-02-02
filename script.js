function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    var chatBody = document.getElementById("chat-body");

    var userMessage = document.createElement("div");
    userMessage.className = "message user-message";
    userMessage.innerHTML = userInput;

    chatBody.appendChild(userMessage);

    document.getElementById("user-input").value = "";

    fetch('http://127.0.0.1:5000/send-message', {  // Change the URL to your backend server address
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        var botMessage = document.createElement("div");
        botMessage.className = "message bot-message";
        botMessage.innerHTML = data.message;
        chatBody.appendChild(botMessage);
    })
    .catch(error => console.error('Error:', error));
}