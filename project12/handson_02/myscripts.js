$('h1').click(function(){
    $(this).text("I was changed!")
})

$("li").click(function() {
    console.log("any li was clicked!");
    
})

$("input").eq(0).keypress(function() {
    $("h3").toggleClass("turnBlue");
})