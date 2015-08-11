// executed after pageload completes
$(function () {
    function successHandler() {
        $('#new_client_form').clearForm();
        $('#new_client').modal('toggle');
    }

    var options = {
        success: successHandler
    };

    $('#new_client_form').ajaxForm(options);
});
