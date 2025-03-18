import { createApp } from "vue";
import "./style.css";
import App from "./app.vue";
import router from "./routes";

const app = createApp(App);

// Utiliser le routeur dans ton application Vue
app.use(router);

app.mount("#app");
