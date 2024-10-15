// var lbs = prompt("Weight in lbs?");
// var kg = lbs * 0.454;
// alert("That is: "+kg+" kilograms");
// console.log("Conversion Complete!");
var hot = false
var temp = 50

if (temp > 80) {
    hot = true
    console.log("Hot outside!");
}else if (temp <= 80 && temp >= 50) {
    console.log("Average temp outside");
    
}else if (temp < 50 && temp >= 32) {
    console.log("It`s pretty cold out");
}else{
    console.log("It is very cold out.");
    
}
