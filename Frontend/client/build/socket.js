const socket1 = new WebSocket("ws://localhost:8765");
const socket2 = new WebSocket("ws://localhost:8766");

//отправляет сообщения
socket1.addEventListener("open", function (event) {
  socket.send("" + mail + "\n" + password + "\n" + login);
});

// Наблюдает за сообщениями
socket2.addEventListener("message", function (event) {
  console.log("Message from server ", event.data);
});
