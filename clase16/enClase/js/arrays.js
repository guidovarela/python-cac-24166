


let animal1 = "leon"
let animal2 = "perro"
let animal3 = "oso"
let animal4 = "raton"

// array / vector / arreglo / matriz
let animales = ["leon","perro","oso","raton", "gato"]
// animales = new Array("leon","perro","oso","raton", "gato")

// document.write(animales[0])
// document.write(animales.length)

//length()
//push()
//pop()
//unshift()
//shift()

function agregarItem(ar){
    data = prompt("Inserte el animal")
    ar.push(data)
    // ar.unshift(data)
}
function quitarItem(ar){
    // ar.pop()
    ar.shift()
}

agregarItem(animales)
agregarItem(animales)
agregarItem(animales)

quitarItem(animales)

// for (let i = 0; i < animales.length; i++) {
//    document.write(animales[i]+"<br>")
// }

// ES6

// for (const key in animales) {
    //     document.write(key+"<br>")
    // }
    
//forEach
const recorrerForEach = animales.forEach(element => {
    console.log(element)
});

for (const iterator of animales) {
    document.write(iterator+"<br>")
}

