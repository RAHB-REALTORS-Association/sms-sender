document.addEventListener('DOMContentLoaded', function() {
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