document.addEventListener('DOMContentLoaded', function() {
    const sidInput = document.getElementById('sid');
    const tokenInput = document.getElementById('token');
    const csvUrlInput = document.getElementById('csv_url');
    const fileInput = document.getElementById('file-upload');
    const sendBtn = document.getElementById('sendBtn');
    const checkmarkSpan = document.getElementById('checkmark');
    const sendIcon = document.getElementById("sendIcon");
    const spinner = document.getElementById("spinner");

    function toggleSendButton() {
        const sidHasValueOrPlaceholder = sidInput.value || sidInput.placeholder;
        const tokenHasValueOrPlaceholder = tokenInput.value || tokenInput.placeholder;
        
        sendBtn.disabled = !(sidHasValueOrPlaceholder && tokenHasValueOrPlaceholder && (fileInput.files.length || csvUrlInput.value));
    }

    sidInput.addEventListener('input', toggleSendButton);
    tokenInput.addEventListener('input', toggleSendButton);
    csvUrlInput.addEventListener('input', toggleSendButton);
    fileInput.addEventListener('change', toggleSendButton);
    
    fileInput.addEventListener('change', function() {
        if (fileInput.files.length > 0) {
            checkmarkSpan.classList.remove('d-none'); // Show checkmark if a file is uploaded.
        } else {
            checkmarkSpan.classList.add('d-none'); // Hide checkmark if no file is uploaded.
        }
    });

    sendBtn.addEventListener("click", function() {
        sendIcon.classList.add("d-none"); // Hide send icon
        spinner.classList.remove("d-none"); // Show spinner
    });

    // Initial toggle of send button state
    toggleSendButton();
});