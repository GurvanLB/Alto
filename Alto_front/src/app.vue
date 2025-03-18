<template>
  <div id="app">
    <!-- Lien vers la page d'accueil -->
    <router-link to="/"></router-link>
    <router-link to="/Accueil"></router-link>
    <!-- Lien vers la page de contact -->
    <router-link to="/Contact"></router-link>

    <!-- Lien vers la page de connexion -->
    <router-link to="/Connexion"></router-link>

    <!-- Lien vers la page de guide -->
    <router-link to="/Guide"></router-link>

    <!-- Afficher le composant correspondant à la route active -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style scoped>
/* Styles pour l'application */
</style>
