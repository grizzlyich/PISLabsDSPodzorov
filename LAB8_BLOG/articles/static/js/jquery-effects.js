$(document).ready(function(){

    $(".post-title").click(function(){
        $(this).next(".post-content").slideToggle();
    });

    $("#show-posts").click(function(){
        $(".post").fadeIn();
    });

    $("#hide-posts").click(function(){
        $(".post").fadeOut();
    });

});