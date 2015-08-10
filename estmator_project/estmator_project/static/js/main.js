$(function () {
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
