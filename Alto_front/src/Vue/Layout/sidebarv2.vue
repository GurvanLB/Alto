<template>
  <div id="sidebar2">
    <!-- Bouton pour ouvrir la sidebar -->
    <button @click="isOpen = true" class="p-2 bg-blue-600 text-white rounded">
      Ouvrir la Sidebar
    </button>

    <!-- Overlay (optionnel, pour assombrir le fond) -->
    <div
      v-if="isOpen"
      class="fixed inset-0 bg-black bg-opacity-50"
      @click="isOpen = false"
    ></div>

    <!-- Sidebar -->
    <aside
      :class="isOpen ? 'translate-x-0' : '-translate-x-full'"
      class="fixed top-0 left-0 h-full w-64 bg-white shadow-lg transform transition-transform duration-300"
    >
      <button @click="isOpen = false" class="p-2 bg-red-600 text-white w-full">
        Fermer
      </button>
      <ul class="p-4">
        <li class="py-2"><a href="#" class="text-blue-600">Accueil</a></li>
        <li class="py-2"><a href="#" class="text-blue-600">Profil</a></li>
        <li class="py-2"><a href="#" class="text-blue-600">Paramètres</a></li>
      </ul>
    </aside>
  </div>
</template>

<script setup>
import { ref } from "vue";

// Définition de l'état pour ouvrir/fermer la sidebar
const isOpen = ref(false);
</script>
