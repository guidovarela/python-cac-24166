
// define el componente
const header = {
    template: `<header class=""></header>`,
    data(){
        return{
            logo:"nuevoLogo"
        }
    }
}

const footer = {
    template: `
    <div class="footer">
        <h4 class="">Curso: {{usuario}}</h4>
        <p>{{anio}}</p>
    </div>
    `,
    data() {
        return { usuario: "Codo a Codo 4.0", anio:2024 }
    }
 }


 

const {createApp} = Vue 
createApp({
    data(){
        return{
            frutas:[
                {nombre:"Manzana", cantidad:50},
                {nombre:"Uva", cantidad:75},
                {nombre:"Mango", cantidad:96},
                {nombre:"Frutilla", cantidad:45}
            ],
            mostrar:true
        }
    },
    components:{
        info:footer,
        header:header
    },
    // Funciones de data binding
    // methods: {
    //     agregarFruta() {
    //         this.frutas.push({ nombre: this.nuevaFruta, cantidad: 0 })
    //         console.log(frutas)
    //     }
    // },
    
}).mount("#app")