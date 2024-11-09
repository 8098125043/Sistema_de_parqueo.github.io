
// script.js

document.getElementById("searchForm").addEventListener("submit", function(event) {
    event.preventDefault();

    // Captura los datos de búsqueda
    const tipo = document.getElementById("tipo").value;
    const marca = document.getElementById("marca").value;
    const modelo = document.getElementById("modelo").value;
    const capacidad = document.getElementById("capacidad").value;

    // Crea un objeto con los datos de búsqueda
    const searchData = {
        tipo: tipo,
        marca: marca,
        modelo: modelo,
        capacidad: capacidad
    };

    // Simula la búsqueda en consola (en un futuro, podrías enviarlo a un backend)
    console.log("Datos de búsqueda:", searchData);
    alert("Búsqueda realizada con los datos: " + JSON.stringify(searchData));
});
