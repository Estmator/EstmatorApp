// executed after pageload completes
$(function () {
    function newClientSuccess() {
        $('#new_client_form').clearForm();
        $('#new_client').modal('toggle');
    }
    function editClientSuccess() {
        $('#edit_client_form').clearForm();
        $('#edit_client').modal('toggle');
    }

    $('#new_client_form').ajaxForm({
        success: newClientSuccess
    });
    $('#edit_client_form').ajaxForm({
        success: editClientSuccess
    });
});
