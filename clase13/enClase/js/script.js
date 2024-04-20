// variable -> var o let
        // constantes -> const

        // let saludo = "chau" + " mundo!"        
        // alert(saludo)
        
        // saludo = 23
        // console.log(saludo)

        // const pi = 3.14159  

        // cuadros de dialogo
        // alert() / prompt() / confirm()
        // "string" + variable -> concatenacion
        // let edadUsuario = prompt("Inserta tu edad: ")
        // document.write("la edad del usuario es:"+edadUsuario)

        // prompt devuelve string
        //parseInt() / parseFloat()
        // let num1 = parseFloat(prompt("insertar el 1er numero"))
        // let num2 = parseFloat(prompt("insertar el 2do numero"))

        // //operadores artimeticos -> + - * /
        // let suma = num1 + num2
        // let resta = num1 - num2
        // let multi = num1 * num2
        // let divi = num1 / num2

        // console.log(suma)

        // let salida = confirm("Estas seguro que queres salir?")
        // let url = "http://google.com"

        // //Condicionales
        // //if(condicion){verdadera}else{falsa}
        // if(salida == true){
        //         window.open(url)
        // }else{
        //         console.log("quiere quedarse ")
        // }
        
        let nota = parseInt(prompt("Inserte la nota: "));
        console.log(nota)

        // Condición
                if ( nota >= 4 && nota <=5) {
                  // Acción A (nota es menor que 5)
                  document.write("Estoy aprobado")
                        }else if(nota >= 6 && nota <=8){
                        // Acción B: (nota es mayor o igual que 5)
                        document.write("Muy buen proyecto ")}else if(nota >= 9){
                        // Acción B: (nota es mayor o igual que 5)
                        document.write("Excelente proyecto")
                        }else{
                                document.write("Desaprobado")
                        }

                        
        
        // //Gabriel ejemplo:
        // document.write( (parseInt(prompt("Inserte la nota: ")) < 5 ? "NO E" : "E") + "stoy aprobado.")

        




             

