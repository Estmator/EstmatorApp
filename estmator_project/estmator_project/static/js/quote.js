function calcSuccess(res) {
    console.log(res);
}

// executed after pageload completes
$(function () {
    //enable number spinner input functionality for each input
    $('#id_travel_time').addClass('spinner-box');
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
            $('.navmenu').offcanvas('toggle');
        });
    });

    $('.quote-submit').click(function () {
        var url = $(this).data('url');
        $('#quote_form').ajaxSubmit({
            url: url,
            success: calcSuccess
        });
        //this prevents normal form submit page navigation
        return false;
    });
});
