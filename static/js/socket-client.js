const socket = io();
const messageInput = document.getElementById("message-input");
const nameInput = document.getElementById("name-input");
const messageContainer = document.getElementById("messages-container");
const sendMsg = () => {
    const messageContent = messageInput.value.trim();
    socket.emit("newMessage", `${nameInput.value}: ${messageContent}`);
    console.log(nameInput.value + messageContent);
    messageInput.value = "";
};

socket.on("newMessage", (msg) => {
    console.log(msg);
    renderNewMsg(msg);
});
const scrollToBottom = (id) => {
    const element = document.getElementById(id);
    element.scrollTop = element.scrollHeight;
};
const renderNewMsg = (newMsg) => {
    const newMsgCard = document.createElement("li");
    newMsgCard.classList.add("list-group-item");
    newMsgCard.innerHTML = `${newMsg}`;
    messageContainer.appendChild(newMsgCard);
    scrollToBottom("messages-container");
};