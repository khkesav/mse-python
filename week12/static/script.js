document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(function(button) {
       button.addEventListener('click', function() {
            alert_message = button.dataset.message;
            alert(alert_message);
       });
    });
})