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
    
    function newCompanySuccess() {
        $('#new_company_form').clearForm();
        $('#new_company').modal('toggle');
    }
    function editCompanySuccess() {
        $('#edit_company_form').clearForm();
        $('#edit_company').modal('toggle');
    }

    $('#new_client_form').ajaxForm({
        success: newClientSuccess
    });
    $('#edit_client_form').ajaxForm({
        success: editClientSuccess
    });

    $('#new_company_form').ajaxForm({
        success: newCompanySuccess
    });
    $('#edit_company_form').ajaxForm({
        success: editCompanySuccess
    });
});
