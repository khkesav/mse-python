document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(function(button) {
       button.addEventListener('click', function() {
            alert_message = button.dataset.message;
            alert(alert_message);
       });
    });

    const previewImage = document.querySelector('.block-image__preview');
    document.getElementById('fileInput').addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const img = document.createElement('img');
                img.src = e.target.result;
                previewImage.appendChild(img);
            };
            reader.readAsDataURL(file);
        }
    });
})