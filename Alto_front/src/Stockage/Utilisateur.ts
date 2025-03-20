import { defineStore } from "pinia";
import axios from "axios";

export const D_Utilisateur = defineStore("utilisateur", {
  state: () => ({
    role: null as string | null,
    id: null as string | null,
    nom: null as string | null,
  }),

  actions: {
    // Fonction pour récupérer les informations utilisateur au démarrage
    async DefUtilisateurDemarage() {
      if (this.id === null || this.role === null || this.nom === null) {
        try {
          const resultat = await axios.get(
            "http://localhost:5000/info_utilisateur",
            {
              withCredentials: true,
            }
          );
          this.role = resultat.data.id_role;
          this.nom = resultat.data.nom;
          this.id = resultat.data.id;
        } catch (error) {
          console.error(
            "Erreur lors de la récupération des données utilisateurs"
          );
        }
      }
    },

    // Fonction pour la connexion d'un utilisateur
    async Connexion(informations: { nom: string; mdp: string }) {
      try {
        // Effectuer la requête de connexion
        const resultat = await axios.post(
          "http://localhost:5000/connecter",
          informations,
          {
            withCredentials: true,
          }
        );

        // Assigner les données de l'utilisateur
        this.role = resultat.data.id_role;
        this.nom = resultat.data.nom;
        this.id = resultat.data.id;
        console.log(this.id);
        console.log(this.nom);
        // Tu pourrais aussi stocker un token si nécessaire
        // localStorage.setItem('auth_token', resultat.data.token);
        return true;
      } catch (error) {
        console.error("Erreur lors de la connexion utilisateur");
        return false;
      }
    },
    // Fonction pour réinitialiser les données utilisateur
    RazUtilisateur() {
      this.id = null;
      this.role = null;
      this.nom = null;
    },
  },
});
