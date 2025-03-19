import { createRouter, createWebHistory } from "vue-router";
import type {
  RouteRecordRaw,
  NavigationGuardNext,
  RouteLocationNormalized,
} from "vue-router"; // Importation de type
import Accueil from "../Vue/accueil.vue";
import Contact from "../Vue/contact.vue";
import Connexion from "../Vue/connexion.vue";
import Guide from "../Vue/guide.vue";
import Recette from "../Vue/recette.vue";
import { verification_jeton } from "../Services/Service"; // Importer la fonction de vérification

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: Connexion,
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
    component: Recette,
    beforeEnter: async (
      to: RouteLocationNormalized, // Type pour "to"
      from: RouteLocationNormalized, // Type pour "from"
      next: NavigationGuardNext // Type pour "next"
    ) => {
      const isAuthenticated = await verification_jeton();
      if (isAuthenticated) {
        next(); // Si le jeton est valide, on laisse passer
      } else {
        next("/Connexion"); // Sinon on redirige vers la page de connexion
      }
    },
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
