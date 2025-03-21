<template>
  <div id="App">
    <!-- Afficher le composant correspondant à la route active -->
    <router-view></router-view>
  </div>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted } from "vue";
import { verifierServeur } from "./Services/Service"; // Importe la fonction

let intervalId: number | null = null;

onMounted(() => {
  // Lancer le ping immédiatement au démarrage
  verifierServeur();

  // Exécuter le ping toutes les 10 secondes
  intervalId = setInterval(verifierServeur, 30000);
});

onUnmounted(() => {
  // Nettoyer l'intervalle quand le composant est détruit
  if (intervalId) clearInterval(intervalId);
});
</script>

<style scoped>
/* Styles pour l'application */
</style>
