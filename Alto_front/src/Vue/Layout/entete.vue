<template>
  <div
    id="entete"
    class="bg-linear-to-t from-primary to-blue-900 drop-shadow-lg"
  >
    <div class="head_pos">
      <!-- Logo Header -->
      <div>
        <img
          class="w-40 m-4"
          src="../Images/alto_prod_logo.png"
          alt="Logo Alto"
        />
      </div>

      <!-- Texte ALTO en arrière-plan -->
      <div class="w-full h-full overflow-hidden">
        <div
          class="flex justify-around opacity-10 w-full h-full items-center text-blue-500"
        >
          <p
            class="text-9xl border-15 font-semibold transform scale-250 truncate"
          >
            ALTO CPSS
          </p>
        </div>
      </div>

      <!-- Interface de connexion header -->
      <div class="flex flex-row items-center m-4">
        <div
          v-if="role > 0"
          class="inline-block w-16 h-16 bg-secondary rounded-full overflow-hidden mr-5"
        >
          <svg
            class="w-full h-full text-gray-300"
            viewBox="0 0 16 16"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <rect
              x="0.62854"
              y="0.359985"
              width="15"
              height="15"
              rx="7.5"
              fill="white"
            ></rect>
            <path
              d="M8.12421 7.20374C9.21151 7.20374 10.093 6.32229 10.093 5.23499C10.093 4.14767 9.21151 3.26624 8.12421 3.26624C7.0369 3.26624 6.15546 4.14767 6.15546 5.23499C6.15546 6.32229 7.0369 7.20374 8.12421 7.20374Z"
              fill="currentColor"
            ></path>
            <path
              d="M11.818 10.5975C10.2992 12.6412 7.42106 13.0631 5.37731 11.5537C5.01171 11.2818 4.69296 10.9631 4.42107 10.5975C4.28982 10.4006 4.27107 10.1475 4.37419 9.94123L4.51482 9.65059C4.84296 8.95684 5.53671 8.51624 6.30546 8.51624H9.95231C10.7023 8.51624 11.3867 8.94749 11.7242 9.62249L11.8742 9.93184C11.968 10.1475 11.9586 10.4006 11.818 10.5975Z"
              fill="currentColor"
            ></path>
          </svg>
        </div>
        <div>
          <button v-if="role === 0" class="bouton">Connexion</button>
          <button v-if="role > 0" class="bouton">Deconnexion</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent, computed } from "vue";

import { D_Utilisateur } from "../../Stockage/Utilisateur";
export default defineComponent({
  setup() {
    const utilisateurStore = D_Utilisateur(); // Récupérer le store Pinia

    // Utiliser une propriété calculée pour accéder à `role` et le convertir en entier
    const role = computed(() => utilisateurStore.role); // Convertir en entier

    console.log("Valeur du role (int):", role.value);

    return {
      role,
    };
  },
});
</script>
