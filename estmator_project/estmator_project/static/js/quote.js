function calcSuccess(res) {
    console.log(res);
}

function showRequest(formdata) {
    console.dir(formdata);
}

function calculateQuote() {
    var totalProducts = 0;
    var subTotal = 0;

    $('.item-row').each(function () {
        var spinner = $(this).find('.spinner-box');
        var count = parseInt(spinner.val());
        totalProducts += count;
        var minutes = count * parseFloat(spinner.data('mins')).toFixed(2);
        subTotal += minutes;

        $(this).find('.calc_mins').html(minutes);
    });

    var totalTruckLoads = (totalProducts / 22).toFixed(2);
    var totalDriveTime = $('#id_travel_time').val() * 2;
    var grandTotal = subTotal + totalDriveTime;
    var totalHours = (grandTotal / 60).toFixed(2);
    var totalDays = (totalHours / 8).toFixed(2);
    var companyVals = $('#companyvals');
    var straightTimeCost = (parseFloat(companyVals.data('straight-time-rate')) * totalHours).toFixed(2);
    var overTimeCost = (parseFloat(companyVals.data('over-time-rate')) * totalHours).toFixed(2);

    $('#genval_totalproducts').html(totalProducts);
    $('#genval_totaltruckloads').html(totalTruckLoads);
    $('#genval_subtotal').html(subTotal);
    $('#genval_totaldrivetime').html(totalDriveTime);
    $('#genval_grandtotal').html(grandTotal);
    $('#genval_totalhours').html(totalHours);
    $('#genval_totaldays').html(totalDays);
    $('#genval_straighttimecost').html(straightTimeCost);
    $('#genval_overtimecost').html(overTimeCost);
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
            $('.reveal-left').offcanvas('toggle');
        });
    });

    //click listener for calculate button
    $('#calculate_btn').click(function () {
        calculateQuote();
    });

    $('.quote-submit').click(function () {
        var url = $(this).data('url');
        $('#quote_form').ajaxSubmit({
            url: url,
            beforeSubmit: showRequest,
            success: calcSuccess
        });
        //this prevents normal form submit page navigation
        return false;
    });

    var reviewButton = $('#review_btn');
    var reviewEnabled = true;
    setInterval(function () {
        if (reviewEnabled && !navigator.onLine) {
            reviewButton.prop('disabled', true);
            reviewButton.removeClass('btn-default');
            reviewButton.addClass('btn-warning');
            reviewEnabled = false;
        } else if (!reviewEnabled && navigator.onLine) {
            reviewButton.prop('disabled', false);
            reviewButton.removeClass('btn-warning');
            reviewButton.addClass('btn-default');
            reviewEnabled = true;
        }
    }, 2000);
});
