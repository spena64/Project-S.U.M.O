// Track user input
const movement = {
	up: false,
	down: false,
	left: false,
	right: false
};
// Track player locations
let players = {};

document.addEventListener('keydown', function(event) {
	switch (event.keyCode) {
		case 65: // A
			movement.left = true;
			break;
		case 87: // W
			movement.up = true;
			break;
		case 68: // D
			movement.right = true;
			break;
		case 83: // S
			movement.down = true;
			break;
	}
});
document.addEventListener('keyup', function(event) {
	switch (event.keyCode) {
		case 65: // A
			movement.left = false;
			break;
		case 87: // W
			movement.up = false;
			break;
		case 68: // D
			movement.right = false;
			break;
		case 83: // S
			movement.down = false;
			break;
	}
});
// Alert server of new player connection
const socket = new WebSocket("ws://localhost:8080/game");
var data = {
    type: "newConnection",
}
socket.send(data);
// Keep server updated with player input
setInterval(function() {
    var data = {
        type: "gameInput",
        body: movement,
    }
    socket.send(data);
}, 1000 / 60);

// Receive game state from server
socket.onmessage = function(event) {
    var msg = JSON.parse(event.data);

    if (msg.type == "gameState") {
        players = msg.body;
    }
};
// Draw game state
const canvas = document.getElementById('canvas');
canvas.width = 800;
canvas.height = 600;
const context = canvas.getContext('2d');
setInterval(function() {
	context.clearRect(0, 0, 800, 600);
	context.fillStyle = 'green';
	for (let id in players) {
		let player = players[id];
		context.beginPath();
		context.arc(player.x, player.y, player.radius, 0, 2 * Math.PI);
		context.fill();
	}
}, 1000 / 60);