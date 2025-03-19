<template>
  <div>
    <entete />
  </div>
  <!--FIN HEADER-->
  <div class="h-full">
    <div class="flex">
      <div>
        <sidebar />
      </div>
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
                <form @submit.prevent="connexion" class="flex flex-col">
                  <label class="font-medium text-gray-800 mb-2">
                    Identifiant :</label
                  >
                  <input
                    v-model="identifiant"
                    class="border-1 w-64 border-gray-400 bg-linear-to-b from-gray-200 via-white via-25% to-white to-90% rounded-sm mb-5"
                    type="text"
                    name="test"
                    id="identifiant"
                    required
                  />
                  <label class="text-gray-800 font-medium mb-2">
                    Mot de passe :</label
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
                      Visible</label
                    >
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
import { connecter } from "../Services/Service";
import router from "../Controleur/routes";

// Déclaration variables
const identifiant = ref("");
const motdepasse = ref("");
const message = ref<string>(""); // Message pour succès ou erreur
const messageClass = ref<string>("text-red-600"); // Couleur du message
//Fonction de connexion
const connexion = async () => {
  const reponse = await connecter(identifiant.value, motdepasse.value);
  // Si la connexion réussit, afficher un message de succès
  if (reponse.error == true) {
    message.value = "Identifiant ou mot de passe incorrect";
  } else {
    router.push("/accueil");
  }
};
</script>
