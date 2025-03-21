import { createRouter, createWebHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router"; // Importation de type
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
    beforeEnter: async (_to, _from, next) => {
      const utilisateur = D_Utilisateur();
      await utilisateur.DefUtilisateurDemarage();
      next(); // Assurez-vous d'appeler next() pour permettre l'accès à la route
    },
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
    beforeEnter: async (_to, _from, next) => {
      const utilisateur = D_Utilisateur();
      await utilisateur.DefUtilisateurDemarage();
      // Vérifie si le rôle est défini et si c'est le bon rôle
      if (utilisateur.role === 1 || utilisateur.role === 2) {
        next();
      } else {
        console.warn("Accès refusé, redirection vers Connexion");
        next({ name: "Connexion" });
      }
    },
  },
  {
    path: "/:pathMatch(.*)*", // Capture toutes les routes inconnues
    redirect: "/Accueil", // Redirige vers une page connue
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
