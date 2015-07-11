$(document).ready(function () {

    $(".mlink").click(function(){
        var target = this.getAttribute('data-target');
        $('html, body').animate({
           scrollTop: $(target).offset().top
        }, 'slow');
    });

    var myVar = setInterval(function () {myTimer()}, 1000);

});

var last_str = '';

function myTimer() {
    
    var str = $('#input').val();

    if (str.length > 90) {
        str = str.substring(0,99);
    }

    var new_str = '';
    if (str != last_str) {
        for (var i = 0, len = str.length; i < len; i++) {
            if (!str[i].match(/[a-z]/i)) {
                new_str = new_str + ' ';
            } else {
                new_str = new_str + str[i];
            }
        }
        var query = 'q=' + encodeURIComponent(new_str);
        $.get('fuzzyapp', query,process);
        last_str = str;
    }
}

function process(data) {
    var obj = jQuery.parseJSON(data);
    var string = '';
    for (var i = 0; i < obj.length; ++i) {
        string += obj[i] + '<br>';
    }
    $('.result').html('<p>' + string + '<\p>');
}
