import { defineStore } from "pinia";
import axios from "axios";

export const D_Utilisateur = defineStore("utilisateur", {
  state: () => ({
    role: 0 as number,
    id: 0 as number,
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
          this.role = resultat.data.role_id;
          this.nom = resultat.data.nom;
          this.id = resultat.data.id;
        } catch (error) {
          return error;
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
        console.log("réponse:", resultat.data);
        // Assigner les données de l'utilisateur
        this.role = resultat.data.role;
        this.nom = resultat.data.nom;
        this.id = resultat.data.id;
        console.log("le role obtenu", this.role);
        return true;
      } catch (error) {
        console.error("Erreur lors de la connexion utilisateur");
        return false;
      }
    },
    // Fonction pour réinitialiser les données utilisateur
    RazUtilisateur() {
      this.id = 0;
      this.role = 0;
      this.nom = null;
    },
    async deconexion() {
      try {
        const resultat = await axios.get("http://localhost:5000/deconnecter", {
          withCredentials: true,
        });
        this.RazUtilisateur();
        return resultat.data;
      } catch (error) {
        return error;
      }
    },
  },
});
