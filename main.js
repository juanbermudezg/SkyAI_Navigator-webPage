document.addEventListener('DOMContentLoaded', function () {
    const navigateButton = document.getElementById('navigateButton');
    navigateButton.addEventListener('click', function () {
        var user=document.getElementById("user").value;
        var email=document.getElementById("email").value;
        var password=document.getElementById("password").value;
        
        window.location.href = 'index.html';
    });
});