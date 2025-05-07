document.addEventListener("DOMContentLoaded", () => {
    const registro_form = document.querySelector('#entrada-form');
    const vehiclePlate = document.querySelector('#vehiclePlate');
    const driverName = document.querySelector('#driverName');
    const entryTime = document.querySelector('#entryTime');
    const parkingSpace = document.querySelector('#parkingSpace');

    registro_form.addEventListener('submit', (event) => {
        event.preventDefault();

        const formData = new FormData();

        formData.append('vehiclePlate', vehiclePlate.value);
        formData.append('driverName', driverName.value);
        formData.append('entryTime', entryTime.value);
        formData.append('parkingSpace', parkingSpace.value);

        fetch('/entrada-vehiculo', {
            method: 'POST',
            body: formData,
        }).then(response => {
            if (response.ok) {
                response.text().then(htmlNewPage => {
                    document.open('', '_self')
                    document.write(htmlNewPage)
                    document.close()
                })
            }
        });
    });
})
