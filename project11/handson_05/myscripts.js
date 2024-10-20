function hello() {
    console.log("Hello World!");
    
}

function helloYou(name) {
    console.log("Hello World "+name);
    
}

function addNum(num1, num2) {
    console.log(num1 + num2);
    
}

function helloSomeone(name="James") {
    console.log("Hello " + name);
    
}

function formal(name="James", title="Sir") {
    return title + " " + name  
}

function fiveTimes(numinput) {
    var result = numinput * 5
    return result
}

var v = " GLOBAL V"
var stuff = "GLOBAL stuff"

function fun(stuff) {
    console.log(v);
    stuff = "Reassign stuff inside function"
    console.log(stuff);
    
}