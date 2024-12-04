const registro_form = document.querySelector('#registro-form');
const login_form = document.querySelector('#login-form');

registro_form.addEventListener('submit', (event) => {
    const formData = new FormData(registro_form);

    if (formData.get('password') !== formData.get('confirmPassword')) {
        alert('Las contrasenas no coinciden');
        event.preventDefault(); // Evita el envío del formulario por defecto
    }
});


login_form.addEventListener('submit', (event) => {
});