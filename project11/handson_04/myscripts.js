var firstName = prompt("First Name please:")
var lastName = prompt("Last Name please: ")
var Age = prompt("How old are you?")
var height = prompt("What is your height?")
var petName = prompt("What is your pet name?")
alert("Thank you for your information")

var nameCond = null;
var ageCond = null;
var heightCond = null;
var petCond = null;

if (firstName[0] === lastName[0]) {
    nameCond = true;
} else {
    nameCond = false;
}

if (age > 20 && age < 30) {
    ageCond = true;4
} else {
    ageCond = false;
}

if (height >= 170 ) {
    heightCond = true
} else {
    heightCond = false
}

if (petName[petName.length-1] === "y") {
    petCond = true
} else {
    petCond = false
}