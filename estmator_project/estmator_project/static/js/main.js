function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++ ) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// executed after pageload completes
$(function () {
    //enable number spinner input functionality for each input
    $(".spinner-box").each(function () {
        $(this).TouchSpin({
            min: 0,
            max: 9999,
            step: 1,
            decimals: 0,
            boostat: 5,
            maxboostedstep: 10
        });
    });

    //add click listeners to each category button
    $(".category_btn").each(function () {
       $(this).click(function () {
           console.log('called');
           $('.navmenu').offcanvas('toggle');
       });
    });
});
