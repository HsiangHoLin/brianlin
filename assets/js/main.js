$(document).ready(function () {

    $(".mlink").click(function(){
        var target = this.getAttribute('data-target');
        $('html, body').animate({
           scrollTop: $(target).offset().top
        }, 'slow');
    });

    var myVar = setInterval(function () {myTimer()}, 2000);

});

