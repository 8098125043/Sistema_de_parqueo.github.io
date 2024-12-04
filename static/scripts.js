const form = document.querySelector('#registro-form');

form.addEventListener('submit', (event) => {
    const formData = new FormData(form);

    if (formData.get('password') !== formData.get('confirmPassword')) {
        alert('Las contrasenas no coinciden');
        event.preventDefault(); // Evita el envío del formulario por defecto
    }
});