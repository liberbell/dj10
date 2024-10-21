var roster = []

function addNew() {
    var newName = prompt("What name would you like to add?");
    roster.push(newName);
}

function remove() {
    var remName = prompt("What name would you like to remove?");
    var index = roster.indexOf(remName);
    roster.splice(index, 1);
}