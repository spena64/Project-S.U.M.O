
// Draw game state
const canvas = document.getElementById('canvas');
canvas.width = 2000;
canvas.height = 1000;
const context = canvas.getContext('2d');

context.rect(1500,500,500,500);
context.stroke();
context.font = "40px Arial";
context.fillText("Player 1", 1650, 200);
context.font = "40px Arial";
context.fillText("------- VS ------", 1600, 250);
context.font = "40px Arial";
context.fillText("Player 2", 1650, 300);
context.strokeStyle = 'red';
context.beginPath();
context.arc(700, 500, 450, 0, 2 * Math.PI);
context.stroke();
