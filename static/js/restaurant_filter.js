function clearField(fieldId) {
    document.getElementById(fieldId).value = "";
    submitForm();
}


function submitForm() {
    document.getElementById('filterForm').submit();
}