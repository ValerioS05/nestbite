//filter form that update the results dynamically when filters are cleared
function clearField(fieldId) {
    document.getElementById(fieldId).value = "";
    submitForm();
}


function submitForm() {
    document.getElementById('filterForm').submit();
}