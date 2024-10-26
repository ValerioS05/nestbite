function fadeAlerts() {
    const alertMessages = document.querySelectorAll('.alert');

    alertMessages.forEach((alertObj, index) => {
        setTimeout(function() {
            alertObj.classList.remove('show');
            alertObj.classList.add('fade');
            setTimeout(function() {
                const alertMessage = new bootstrap.Alert(alertObj);
                alertMessage.close();
            }, 300);
        }, 4000 + (index * 1000)); // Add delay for each alert message in successiom
    });
}

document.addEventListener('DOMContentLoaded', fadeAlerts);