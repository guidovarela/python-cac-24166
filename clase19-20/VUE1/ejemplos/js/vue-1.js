let mensaje = "Hola desde Vue"

const {createApp} = Vue 
createApp({
    data(){
        return{
            mensaje:mensaje,
            titulo:"<i>Codo a Codo</i>",
            data_principal: `<p> mucho texto mucho texto mucho texto mucho texto mucho texto mucho texto <br> mas texto mas textomas texto</p>`,
        }
    }
}).mount("#app")


// const {createApp} = Vue 
// createApp({
//     data(){
//         return{
//             nombre:"Juan",
//             apellido: "Perez",
//         }
//     }
// }).mount("#ejemplo1")
