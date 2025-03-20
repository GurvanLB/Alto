import { createApp } from "vue";
import "./style.css";
import App from "./app.vue";
import router from "./Controleur/routes";
import { createPinia } from "pinia";

const app = createApp(App);

// Initialisation du store Pinia
const pinia = createPinia();
app.use(pinia);

// Initialisation de Vue Router
app.use(router);

// Montage de l'application
app.mount("#app");
