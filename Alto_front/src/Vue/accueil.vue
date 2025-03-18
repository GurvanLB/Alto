<template>
  <div>
    <Entete />
  </div>
  <!-- FIN HEADER-->
  <div class="h-full">
    <div class="flex h-full">
      <!--SIDEBAR-->
      <div>
        <sidebar />
      </div>
      <!-- FIN SIDEBAR-->
      <div id="Body" class="flex flex-1 w-full justify-center bg-secondary">
        <div
          class="flex flex-1 flex-col max-w-[1000px] bg-secondary h-full m-4"
        >
          <!-- BREADCRUMB -->
          <div>
            <breadcrumb onglet="Général" page="Accueil" />
          </div>
          <!-- FIN BREADCRUMB-->
          <!--::::::::::::::::::::::::::::::CONTENT::::::::::::::::::::::::::::::::::::::::-->
          <!--Carroussel-->
          <div class="carousel-container mt-10 mb-10">
            <div
              class="w-full h-100 overflow-hidden relative rounded-lg shadow-lg"
            >
              <!-- Inputs radio pour naviguer -->
              <input
                type="radio"
                name="carousel"
                id="slide1"
                class="hidden peer/slide1"
                checked
              />
              <input
                type="radio"
                name="carousel"
                id="slide2"
                class="hidden peer/slide2"
              />
              <input
                type="radio"
                name="carousel"
                id="slide3"
                class="hidden peer/slide3"
              />

              <!-- Conteneur des images -->
              <div
                class="flex w-full h-100 transition-transform duration-500 peer-checked/slide1:translate-x-0 peer-checked/slide2:-translate-x-full peer-checked/slide3:-translate-x-[200%]"
              >
                <img
                  src="./Images/carrousel.jpg"
                  class="w-full h-h-100 object-cover flex-shrink-0"
                />
                <img
                  src="./Images/abri-home-1024x599-1.png"
                  class="w-full h-100 object-cover flex-shrink-0"
                />
                <img
                  src="./Images/terrain.jpg"
                  class="w-full h-100 object-cover flex-shrink-0"
                />
              </div>
              <!-- Navigation par boutons -->
              <div
                class="absolute bottom-2 left-0 right-0 flex justify-center space-x-2"
              >
                <label
                  for="slide1"
                  class="w-3 h-3 bg-gray-300 rounded-full cursor-pointer hover:bg-gray-500 transition"
                ></label>
                <label
                  for="slide2"
                  class="w-3 h-3 bg-gray-300 rounded-full cursor-pointer hover:bg-gray-500 transition"
                ></label>
                <label
                  for="slide3"
                  class="w-3 h-3 bg-gray-300 rounded-full cursor-pointer hover:bg-gray-500 transition"
                ></label>
              </div>
            </div>
          </div>
          <!--  3 Cartes -->
          <div class="flex flex-wrap justify-center">
            <div class="cards">
              <h3 class="text-lg font-bold text-gray-800 dark:text-white">
                Card title
              </h3>
              <p
                class="mt-1 text-xs font-medium uppercase text-gray-500 dark:text-neutral-500"
              >
                Card subtitle
              </p>
              <p class="mt-2 text-gray-500 dark:text-neutral-400">
                Some quick example text to build on the card title and make up
                the bulk of the card's content.
              </p>
            </div>
            <div class="cards">
              <h3 class="text-lg font-bold text-gray-800 dark:text-white">
                Card title
              </h3>
              <p
                class="mt-1 text-xs font-medium uppercase text-gray-500 dark:text-neutral-500"
              >
                Card subtitle
              </p>
              <p class="mt-2 text-gray-500 dark:text-neutral-400">
                Some quick example text to build on the card title and make up
                the bulk of the card's content.
              </p>
            </div>
            <div class="cards">
              <h3 class="text-lg font-bold text-gray-800 dark:text-white">
                Production
              </h3>
              <p
                class="mt-1 text-xs font-medium uppercase text-gray-500 dark:text-neutral-500"
              >
                Gestion recette
              </p>
              <p class="mt-2 text-gray-500 dark:text-neutral-400">
                Cette interface permet la modification des données.
              </p>
            </div>
          </div>

          <!--Diviseur-->
          <div class="flex justify-center w-full mt-4">
            <hr class="hr sm:w-1/2 lg:w-2/3 xl:w-full mt-10" />
          </div>

          <!-- Carte -->
          <div class="w-full flex flex-col items-center mt-20 mb-20">
            <!-- Présentation de la machine -->
            <div
              class="bg-white border-1 border-gray-300 rounded-xl shadow-sm sm:flex mr-4 ml-4 w-full"
            >
              <div
                class="shrink-0 relative w-full rounded-t-xl overflow-hidden pt-[30%] sm:rounded-s-xl sm:max-w-80 md:rounded-se-none md:max-w-sm"
              >
                <img
                  class="size-full absolute top-0 start-0 object-cover border-gray-200 rounded-2xl"
                  src="./Images/terrain.jpg"
                  alt="Card Image"
                />
              </div>
              <div class="flex flex-wrap">
                <div class="p-4 flex flex-col h-full sm:p-7">
                  <h3 class="text-lg font-bold text-gray-800 dark:text-white">
                    Présentation machine
                  </h3>
                  <p
                    class="mt-1 text-xs font-medium uppercase text-gray-500 dark:text-neutral-500"
                  >
                    Card subtitle
                  </p>
                  <p class="mt-1 text-gray-500 dark:text-neutral-400 text-wrap">
                    Some quick example text to build on the card title and make
                    up the bulk of the card's content.
                  </p>
                </div>
              </div>
            </div>
          </div>
          <!--:::::::::::::::::::::::::::::: FIN CONTENT::::::::::::::::::::::::::::::::::::::::-->
        </div>
      </div>
    </div>
  </div>
  <!-- FIN BODY-->
  <div>
    <foot />
  </div>
  <!-- FIN FOOTER-->
</template>

<script setup lang="ts">
import sidebar from "./Layout/sidebar.vue";
import Entete from "./Layout/entete.vue";
import foot from "./Layout/foot.vue";
import breadcrumb from "./Layout/breadcrumb.vue";
</script>
