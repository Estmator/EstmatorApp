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
    $('#genval_subtotal').html(subTotal + ' mins');
    $('#quote_subtotal').val(subTotal);
    $('#genval_totaldrivetime').html(totalDriveTime + ' mins');
    $('#genval_grandtotal').html(grandTotal + ' mins');
    $('#quote_grandtotal').val(grandTotal);
    $('#genval_totalhours').html(totalHours);
    $('#genval_totaldays').html(totalDays);
    $('#genval_straighttimecost').html('$' + straightTimeCost);
    $('#quote_straighttimecost').val(straightTimeCost);
    $('#genval_overtimecost').html('$' + overTimeCost);
    $('#quote_overtimecost').val(overTimeCost);
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

        $(this).change(function () {
            disableReviewButton();
        });
    });

    //add click listeners to each category button
    $(".category_btn").each(function () {
        $(this).click(function () {
            var category_id = $(this).data('category-id');
            var offset = $(category_id).offset();
            setTimeout(function () {
                $(window).scrollTop(offset.top - 50);
            }, 500);
            if ($('.reveal-left').css('width') == '180px') {
                $('.reveal-left').offcanvas('toggle');
            }
        });
    });

    //click listener for calculate button
    $('#calculate_btn').click(function () {
        calculateQuote();
        enableReviewButton();
    });

    var reviewButton = $('#review_btn');
    var reviewButtonEnabled = true;
    var reviewButtonInterval = null;
    //review button is disabled at start, available again upon calculation
    disableReviewButton();

    function disableReviewButton() {
        if (reviewButtonEnabled) {
            reviewButton.prop('disabled', true);
            reviewButton.removeClass('btn-warning');
            reviewButton.addClass('btn-default');
            reviewButtonEnabled = false;
            clearInterval(reviewButtonInterval);
        }
    }

    function enableReviewButton() {
        if (!reviewButtonEnabled) {
            reviewButton.prop('disabled', false);
            reviewButton.removeClass('btn-warning');
            reviewButton.addClass('btn-default');
            reviewButtonEnabled = true;
            reviewButtonInterval = setInterval(checkIfOnline, 2000);
        }
    }

    function warningReviewButton() {
        if (reviewButtonEnabled) {
            reviewButton.prop('disabled', true);
            reviewButton.removeClass('btn-default');
            reviewButton.addClass('btn-warning');
            reviewButtonEnabled = false;
        }
    }

    function checkIfOnline() {
        $.ajax({
            url: '/connection-test',
            success: enableReviewButton,
            error: warningReviewButton
        });
    }
});
