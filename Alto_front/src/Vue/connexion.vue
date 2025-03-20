<template>
  <div>
    <entete />
  </div>
  <!-- FIN HEADER-->
  <div class="h-full">
    <div class="flex">
      <sidebar />
      <!-- FIN SIDEBAR-->
      <div id="Body" class="flex flex-1 w-full justify-center bg-secondary">
        <div
          class="flex flex-1 flex-col max-w-[1000px] bg-secondary h-full m-4"
        >
          <!--::::::::::::::::::::::::::::::CONTENT::::::::::::::::::::::::::::::::::::::::-->
          <div class="flex h-full w-full flex-col items-center mb-50">
            <div
              v-if="message"
              :class="messageClass"
              class="w-full mb-4 p-4 bg-red-200 border-2 text-center border-red-500 rounded-md shadow-md"
            >
              {{ message }}
            </div>
            <div class="cardsbig w-ufll h-120 justify-center flex-col">
              <div
                class="text-primary flex justify-center text-4xl font-bold sm:mb-5"
              >
                <h1>Connexion</h1>
              </div>
              <div class="flex justify-center mt-10">
                <form @submit.prevent="connecter" class="flex flex-col">
                  <label class="font-medium text-gray-800 mb-2"
                    >Identifiant :</label
                  >
                  <input
                    v-model="identifiant"
                    class="border-1 w-64 border-gray-400 bg-linear-to-b from-gray-200 via-white via-25% to-white to-90% rounded-sm mb-5"
                    type="text"
                    name="identifiant"
                    id="identifiant"
                    required
                  />
                  <label class="text-gray-800 font-medium mb-2"
                    >Mot de passe :</label
                  >
                  <input
                    v-model="motdepasse"
                    class="border-1 border-gray-400 bg-linear-to-b from-gray-200 via-white via-25% to-white to-90% rounded-sm mb-2"
                    type="password"
                    name="motdepasse"
                    id="motdepasse"
                    required
                  />
                  <div class="flex items-center mb-10">
                    <input type="checkbox" class="flex" />
                    <label
                      class="font-extralight text-sm italic text-gray-800 ml-2"
                    >
                      Visible
                    </label>
                  </div>
                  <button
                    type="submit"
                    class="bg-primary hover:bg-blue-700 rounded-sm border-1 p-2 text-secondary font-bold"
                  >
                    Connexion
                  </button>
                </form>
              </div>
            </div>
          </div>
          <!--::::::::::::::::::::::::::::::FIN CONTENT::::::::::::::::::::::::::::::::::::::::-->
        </div>
      </div>
    </div>
  </div>
  <div>
    <foot />
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import entete from "./Layout/entete.vue";
import foot from "./Layout/foot.vue";
import sidebar from "./Layout/sidebar.vue";
import { D_Utilisateur } from "../Stockage/Utilisateur"; // Importer le store Pinia
import { useRouter } from "vue-router"; // Importer useRouter pour la navigation
import type { Axios, AxiosResponse } from "axios";

// Déclarer les variables pour le formulaire
const identifiant = ref("");
const motdepasse = ref("");
const message = ref<string | null>(null);
const messageClass = ref("");

// Récupérer l'instance du store Pinia
const utilisateurStore = D_Utilisateur();
const router = useRouter();

// Fonction pour la connexion
const connecter = async () => {
  const information = {
    nom: identifiant.value,
    mdp: motdepasse.value,
  };
  const resultat: AxiosResponse | null;
  // Appeler la méthode de connexion du store
  resultat = await utilisateurStore.Connexion(information);

  if (utilisateurStore.id != null) {
    router.push({ name: "Accueil" });
  } else {
    message.value = resultat;
  }
  // Si la connexion est réussie, rediriger vers la page Accueil
};
</script>
