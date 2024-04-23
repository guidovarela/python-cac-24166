/*
Utilizamos un bucle for para imprimir números del 1 al 5 en la consola. 
El bucle for tiene una variable de control i que comienza en 1, verifica si i es menor o igual a 5 en cada iteración y aumenta i en 1 en cada ciclo.
*/

// for(iniciador;condicion;incremento){}

for (let i = 0; i <= 100; i=i+10) {
    // console.log(i);
    document.write(i+"<br>")
}

// i=1
// while(i <= 100){
//     document.write(i+"<br>")
//     i++
// }






// Ejemplo de bucle while
/*
Finalmente, utilizamos un bucle while para lograr el mismo resultado que el bucle for. El bucle while verifica una condición (en este caso, si contador es menor o igual a 5) y ejecuta el bloque de código mientras la condición sea verdadera. Luego, aumentamos contador en cada iteración.
*/
console.log("Imprimir números del 1 al 5 usando un bucle while:");
let contador = 1;

while (contador <= 5) {
    console.log(contador);
    contador++;
}