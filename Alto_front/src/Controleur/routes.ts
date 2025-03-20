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
// Importer la fonction de vérification
import { D_Utilisateur } from "../Stockage/Utilisateur";

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
    beforeEnter: async (to, from, next) => {
      const utilisateur = D_Utilisateur();
      await utilisateur.DefUtilisateurDemarage();
      console.log(utilisateur.role);
      if (utilisateur.role === "1") {
        next();
      } else {
        next({ name: "Connexion" });
      }
    },
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
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
