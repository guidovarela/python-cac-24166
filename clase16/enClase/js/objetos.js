// objetos

// let objeto = {propiedad: "valor"} 
function saludar1(){
    alert("Hola!")
}

let persona = {
    nombre:"Guido",
    apellido:"Carrillo",
    edad: 28,
    saludar: function () {
        alert("Hola!")
    }
}

// DOM - Document Object Model

let caja = document.querySelector("#persona")
caja.innerHTML="Hola, mi nombre es "+persona.nombre+" "+persona.apellido+" <br> Tengo "+persona.edad+" años.<a href='#' onclick='"+persona.saludar+"'>Saludar</a>"
