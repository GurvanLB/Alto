import { createRouter, createWebHistory } from "vue-router";
import Accueil from "./Vue/accueil.vue";
import Contact from "./Vue/contact.vue";
import Connexion from "./Vue/connexion.vue";
import Guide from "./Vue/guide.vue";
import recette from "./Vue/recette.vue";
const routes = [
  {
    path: "/",
    name: "/",
    component: Accueil,
  },
  {
    path: "/Accueil",
    name: "Accueil",
    component: Accueil,
  },
  {
    path: "/Contact",
    name: "Contact",
    component: Contact,
  },
  {
    path: "/Connexion",
    name: "Connexion",
    component: Connexion,
  },
  {
    path: "/Guide",
    name: "Guide",
    component: Guide,
  },
  {
    path: "/Recette",
    name: "Recette",
    component: recette,
  },
  //liste des routes
];
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
