let submitButton = document.getElementById("submit-button");

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

document.addEventListener("DOMContentLoaded", function(event) {
    submitButton.addEventListener("click", function(event) {
        for (let i = 0; i < 1000000; i++) {
            console.log(i);
        }
        window.location.href = "/thank_you";
    });
});
