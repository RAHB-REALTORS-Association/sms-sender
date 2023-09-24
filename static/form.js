document.addEventListener('DOMContentLoaded', function() {
    const alert = document.getElementById('disclaimer');
    const fileInput = document.getElementById('file-upload');
    const sendBtn = document.getElementById('sendBtn');
    const checkmarkSpan = document.getElementById('checkmark');
    const sendIcon = document.getElementById("sendIcon");
    const spinner = document.getElementById("spinner");
    
    // Check if the alert has been dismissed.
    if (sessionStorage.getItem('alertDismissed') === 'true') {
        alert.style.display = 'none';
    }
    
    // Listen for the close event of the alert.
    alert.addEventListener('close.bs.alert', function() {
        // When the alert is dismissed, set the item in sessionStorage.
        sessionStorage.setItem('alertDismissed', 'true');
    });
    
    fileInput.addEventListener('change', function() {
        if (fileInput.files.length > 0) {
            // Show checkmark if a file is uploaded.
            checkmarkSpan.classList.remove('d-none');
        } else {
            // Hide checkmark if no file is uploaded.
            checkmarkSpan.classList.add('d-none');
        }
    });

    sendBtn.addEventListener("click", function() {
        sendIcon.classList.add("d-none"); // Hide send icon.
        spinner.classList.remove("d-none"); // Show spinner.
    });
});