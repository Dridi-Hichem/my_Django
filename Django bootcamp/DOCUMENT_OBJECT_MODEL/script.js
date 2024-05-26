// Restart part
var tableCells = document.getElementsByTagName("td");

function restart() {
  for (cell of tableCells) {
    cell.textContent = "";
  }
}

var restartButton = document.getElementById("restart");

restartButton.addEventListener("click", restart)


// Cell fill
function addX() {
  this.textContent = "X";
}

function addO() {
  this.textContent = "O";
}

for (cell of tableCells) {
  cell.addEventListener("click", addX);
  cell.addEventListener("dblclick", addO);
}
