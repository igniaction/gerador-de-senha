function copyPassword() {
    const passwordText = document.getElementById('generated-password').textContent;
    navigator.clipboard.writeText(passwordText).then(function() {
        document.getElementById('copy-text').textContent = 'Senha Copiada';
    }, function(err) {
        alert('Failed to copy password');
    });
}

function clearForm() {
    document.getElementById('password-form').reset();
    document.getElementById('generated-password').textContent = '';
    document.getElementById('copy-text').textContent = 'Copiar Senha';
}
