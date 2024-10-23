var restart = document.querySelector('#abc');

var squares = document.querySelectorAll('td');

function clearBoard() {
    for (var i = 0; i < squares.length; i++) {
        squares[i].textContent = '';
        
    }
}
restart.addEventListener('click', clearBoard);

function changeMarker() {
    if (this.textContent === '') {
        this.textContent = 'X';
    } else if (this.textContent === 'X') {
        this.textContent = 'O';
    }
}

var cellOne = document.querySelector('#one');
cellOne.addEventListener('click', function() {
    if (cellOne.textContent === "") {
        cellOne.textContent = "X";   
    } else if (cellOne.textContent === "X") {
        cellOne.textContent = "o";
    } else {
        cellOne.textContent = "";
    }
})