// console.log("1 x 0 = ", 1 * 0);
// console.log("1 x 1 = ", 1 * 1);
// console.log("1 x 2 = ", 1 * 2);
// console.log("1 x 3 = ", 1 * 3);
// console.log("1 x 4 = ", 1 * 4);
// console.log("1 x 5 = ", 1 * 5);
// console.log("1 x 6 = ", 1 * 6);
// console.log("1 x 7 = ", 1 * 7);
// console.log("1 x 8 = ", 1 * 8);
// console.log("1 x 9 = ", 1 * 9);
// console.log("1 x 10 = ", 1 * 10);

// for (i = 1; i < 11; i++) {
//     console.log("1 x", i, "=", 1 * i);
// }

// // Primera vez
// for (i = 1; i <= 10; i++) {console.log("1 x", i, "=", 1 * i);}
// // Segunda vez
// for (i = 1; i <= 10; i++) {console.log("1 x", i, "=", 1 * i);}
// // Tercera vez
// for (i = 1; i <= 10; i++) {console.log("1 x", i, "=", 1 * i);}

//Declaración de la función tablaDelUno()
function tablaDelUno() {
    for (i = 1; i <= 10; i++) {
        console.log("1 x", i, "=", 1 * i);
    }
}

// funciones con parametros o argumentos
function tablas(num, hasta){
    for (i = 1; i <= hasta; i++) {
            console.log(num, "x", i, "=", num * i);
        }
}

function tablas2(hasta){
    num2 = Number(prompt("Insertar un numero"))
    for (i = 1; i <= hasta; i++) {
            console.log(num2, "x", i, "=", num2 * i);
        }
}

let nombre = "Pepe"

function saludar(){
    //ambito local
    nombre = prompt("Nombre: ")
    alert("Hola "+nombre)
}

console.log(nombre)







//Bucle que ejecuta 3 veces la función tablaDelUno()
// for (let i = 1; i <= 3; i++) { tablaDelUno(); }