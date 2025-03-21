import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import router from "./Controleur/routes";
import { createPinia } from "pinia";
const pinia = createPinia();

const app = createApp(App);
app.use(pinia);
// Initialisation du store Pinia

// Initialisation de Vue Router
app.use(router);

// Montage de l'application
app.mount("#app");
