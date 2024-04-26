let libros = [
    {
        titulo: "El Gran Gatsby",
        autor: "F. Scott Fitzgerald",
        lanzamiento: 1925,
        cantidad:23
    },
    {
        titulo: "Cien años de soledad",
        autor: "Gabriel García Márquez",
        lanzamiento: 1967,
        cantidad:55
    },
    {
        titulo: "1984",
        autor: "George Orwell",
        lanzamiento: 1949,
        cantidad:12
    }
];

let caja = document.querySelector("#libros-oferta")

for (const data of libros) {
    // caja.innerHTML+=data.titulo+"<br>"+data.autor+"<br>"+data.lanzamiento+""+data.cantidad+"<hr>"

    // template strings
    caja.innerHTML+=`<div class="libro">
    <h3>${data.titulo}</h3> ${data.autor} <br> ${data.lanzamiento} <br>Cantidad de ejemplares: ${data.cantidad}</div>`
}

