// $('h1').click(function(){
//     $(this).text("I was changed!")
// })

// $("li").click(function() {
//     console.log("any li was clicked!");
    
// })

// $("input").eq(0).keypress(function(event) {
//     $("h3").toggleClass("turnBlue");
//     console.log(event);
//     if (event.which === 13) {
//         $("h3").toggleClass("turnRed");
//     }
// })

// $("h1").on("mouseenter", function() {
//     $(this).toggleClass("turnBlue")
// })

$("input").eq(0).on("click", function() {
    $(".container").fadeout(3000)
})