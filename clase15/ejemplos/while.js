/*Bucle WHILE*/

// i = 0; // Inicialización de la variable contador
// // Condición: Mientras la variable contador sea menor de 5
// while (i < 5) {
//   console.log("Valor de i:", i);
//   i = i + 1; // Incrementamos el valor de i (Alternativa: i++)
// }

//Otro ejemplo: Leer notas hasta que ingrese -1
let nota=0;
// nota=Number(prompt("Ingrese una nota (para finalizar ingrese -1):"));

while (nota != -1){//mientras la nota no sea -1
  nota=Number(prompt("Ingrese una nota (para finalizar ingrese -1):" ));
  
  if(nota > 10 && nota != null){
    document.write("numero fuera de rango"+"<br>")
  }  else if(nota >= 6){
      document.write("Tu nota es: " + nota + ", estas aprobado<br>")
    }else{
      document.write("Tu nota es: " + nota + ", estas desaprobado<br>")
    }
}

