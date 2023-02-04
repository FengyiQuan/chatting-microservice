const socket = io();
const messageInput = document.getElementById("message-input");
const nameInput = document.getElementById("name-input");
const messageContainer = document.getElementById("messages-container");
const username = nameInput.value;
const sendMsg = () => {
    const messageContent = messageInput.value.trim();
    socket.emit("send_message", {
        username,
        room: roomId,
        message: messageContent
    });
    console.log(messageInput.value + messageContent);
    messageInput.value = "";
};
socket.on('connect', function () {
    socket.emit('join_room', {
        username,
        room: roomId
    });
});

socket.on('join_room_announcement', function (data) {
    console.log(data);
    if (data.username !== username) {
        const newNode = document.createElement('div');
        newNode.innerHTML = `<b>${data.username}</b> has joined the room`;
        messageContainer.appendChild(newNode);
    }
});

socket.on('leave_room_announcement', function (data) {
    console.log(data);
    const newNode = document.createElement('div');
    newNode.innerHTML = `<b>${data.username}</b> has left the room`;
    messageContainer.appendChild(newNode);
});

window.onbeforeunload = function () {
    socket.emit('leave_room', {
        username,
        room: roomId
    })
};

socket.on("receive_message", (msg) => {
    console.log('receive_message', msg);
    renderNewMsg(msg);
});
const scrollToBottom = (id) => {
    const element = document.getElementById(id);
    element.scrollTop = element.scrollHeight;
};
const renderNewMsg = (newMsg) => {
    const newMsgCard = document.createElement("li");
    newMsgCard.classList.add("list-group-item");
    newMsgCard.innerHTML = `${newMsg.username}: ${newMsg.message}`;
    messageContainer.appendChild(newMsgCard);
    scrollToBottom("messages-container");
};