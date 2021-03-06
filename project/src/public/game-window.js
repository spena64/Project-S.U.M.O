// Track user input
const movement = {
	up: false,
	down: false,
	left: false,
	right: false
};
// Track player locations
let players = {};
let playerNames = [];

// Listeners for keyboard input
document.addEventListener('keydown', function(event) {
	switch (event.keyCode) {
		case 37: // Left arrow
		case 65: // A
			movement.left = true;
			break;
		case 38: // Up arrow
		case 87: // W
			movement.up = true;
			break;
		case 39: // Right arrow
		case 68: // D
			movement.right = true;
			break;
		case 40: // Down arrow
		case 83: // S
			movement.down = true;
			break;
	}
});
document.addEventListener('keyup', function(event) {
	switch (event.keyCode) {
		case 37: // Left arrow
		case 65: // A
			movement.left = false;
			break;
		case 38: // Up arrow
		case 87: // W
			movement.up = false;
			break;
		case 39: // Right arrow
		case 68: // D
			movement.right = false;
			break;
		case 40: // Down arrow
		case 83: // S
			movement.down = false;
			break;
	}
});

// Establish websocket connection
const userID = Math.random().toString(36).substring(2);
const ws = new WebSocket("wss://game-server-staging.herokuapp.com/");
let socketOpen = false;

let matchType = "duo"

ws.onopen = function() {
    console.log("WebSocket connected.");
    socketOpen = true;
    var data = {
        type: "newConnection",
        id: userID
    }
    ws.send(JSON.stringify(data));
    data = {
        type: "enqueue",
        body: matchType
    }
    ws.send(JSON.stringify(data));

    setInterval(sendInput, 1000 / 60);
}

// Keep server updated with player input
sendInput = function() {
    if (socketOpen) {
        var data = {
            type: "gameInput",
            body: movement
        }
        ws.send(JSON.stringify(data));
    }
};

// Receive info from server
ws.onmessage = function(event) {
	var msg = JSON.parse(event.data);

    if (msg.type == "info") {
        console.log(msg.body);
    }
    if (msg.type == "gameState") {

        document.querySelector(".loader").style.display = "none";

        players = msg.body.playerData;
        playerNames = msg.body.playerNames;
        
        if (msg.body.matchData.state == "finished") {
            if (msg.body.matchData.youWin == true) {
                document.querySelector("#match-end-message").innerHTML = "You win!";
                document.querySelector(".modal-content").style.backgroundColor = "#A6EBED";
            } else {
                document.querySelector("#match-end-message").innerHTML = "You lost to " + msg.body.matchData.winner + "!";
                document.querySelector(".modal-content").style.backgroundColor = "#F1A9F2";
            }
            document.querySelector(".modal").style.display = "block";
        }
    }
};

ws.onclose = function() {
    socketOpen = false;
    console.log("Connection closed.")
};

// Draw game state
const canvas = document.getElementById('canvas');
canvas.width = 2000;
canvas.height = 1000;
const context = canvas.getContext('2d');

setInterval(function() {
    context.clearRect(0, 0, 2000, 1000);
    
    // Draw chat box
    context.strokeStyle = 'magenta';
    context.beginPath();
    context.rect(1500,500,500,500);
    context.stroke();

    // Draw text
    context.fillStyle = 'white';
    context.font = "40px Arial";
    context.fillText("------- VS ------", 1600, 250);

    playerIds = Object.keys(players)

    context.fillStyle = players[playerIds[0]].color;
    context.fillText(playerNames[0], 1650, 200);

    context.fillStyle = players[playerIds[1]].color;
    context.fillText(playerNames[1], 1650, 300);

    // Draw ring
    context.strokeStyle = '#1BEBED';
    context.beginPath();
    context.arc(700, 500, 450, 0, 2 * Math.PI);
    context.stroke();

    // Draw players
    for (let id in players) {
        let player = players[id];
        context.fillStyle = player.color;
        context.beginPath();
        context.arc(player.x, player.y, player.radius, 0, 2 * Math.PI);
        context.fill();
    }
}, 1000 / 60);