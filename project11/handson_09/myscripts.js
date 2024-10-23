var restart = document.querySelector('#abc');

var squares = document.querySelectorAll('td');

function clearBoard() {
    for (var i = 0; i < squares.length; i++) {
        squares[i].textContent = '';
        
    }
}
restart.addEventListener('click', clearBoard);

var callOne = document.querySelector('#one');
callOne.addEventListener('click', function() {
    callOne.textContent = "X";
})