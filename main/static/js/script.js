


$(document).ready(function() {
    setTimeout(function() {
        $('.fade').fadeOut(1500);
    }, 3000);
});



function validateForm() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm_password").value;

    if (password !== confirmPassword) {
        alert("Las contraseñas no coinciden. Por favor, verifica.");
        return false;
    }
    return true;
}