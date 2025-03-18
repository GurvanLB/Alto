<template>
  <div>
    <Entete />
  </div>
  <!-- FIN HEADER-->
  <div class="h-full">
    <div class="flex h-full">
      <div>
        <sidebar />
      </div>
      <!-- FIN SIDEBAR-->
      <div id="Body" class="flex flex-1 w-full justify-center bg-secondary">
        <div
          class="flex flex-1 flex-col max-w-[1000px] bg-secondary h-full m-4"
        >
          <div>
            <breadcrumb onglet="Général" page="Contact" />
          </div>
          <!--FIN BREADCRUMB-->
          <!--::::::::::::::::::::::::::::::CONTENT::::::::::::::::::::::::::::::::::::::::-->
          <div
            class="flex justify-around flex-wrap-reverse items-center w-full mt-10"
          >
            <div class="cards">
              <h3 class="text-lg font-bold text-gray-800 dark:text-white">
                Roty&Fils
              </h3>
              <p
                class="mt-1 text-xs font-medium uppercase text-gray-500 dark:text-neutral-500"
              >
                Fabricant de machines
              </p>
              <p class="mt-2 text-gray-500 dark:text-neutral-400">
                Cette interface permet la modification des données.
              </p>
            </div>
            <div class="flex w-80 max-h-30">
              <!--Logo Footer-->
              <img
                fetchpriority="high"
                decoding="async"
                width="1497"
                height="500"
                src="https://www.roty-tyro.com/wp-content/uploads/2023/11/ROTY-2023-Baseline-RVB.png"
                class="flex"
              />
            </div>
          </div>

          <!--DIVSEURR 1-->
          <div class="flex justify-center w-full mt-4">
            <hr class="hr sm:w-1/2 lg:w-2/3 xl:w-full mt-10" />
          </div>
          <div class="flex flex-wrap justify-around mt-10">
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
          </div>
          <!--DIVSEURR 2-->
          <div class="flex justify-center w-full mt-4">
            <hr class="hr sm:w-1/2 lg:w-2/3 xl:w-full mt-10" />
          </div>
          <div class="w-full flex flex-col items-center mt-20 mb-20">
            <!-- Carte map-->
            <div
              class="bg-white border-1 border-gray-300 rounded-xl shadow-sm md:flex mr-4 ml-4 w-full"
            >
              <div
                class="shrink-0 relative w-full rounded-t-xl overflow-hidden pt-[30%] sm:rounded-s-xl sm:max-w-80 md:rounded-se-none md:max-w-sm"
              >
                <img
                  class="size-full absolute top-0 start-0 object-cover border-gray-200 rounded-2xl"
                  src="https://www.roty-tyro.com/wp-content/uploads/2021/03/localisation_roty.jpg"
                  alt="Card Image"
                />
              </div>
              <div class="flex flex-wrap">
                <div class="p-4 flex flex-col h-full sm:p-7">
                  <h3 class="text-lg font-bold text-gray-800 dark:text-white">
                    Nous rendre visite
                  </h3>
                  <p
                    class="mt-1 text-xs font-medium uppercase text-gray-500 dark:text-neutral-500 mb-4"
                  >
                    Adresse
                  </p>
                  <p
                    class="mt-1 text-primary font-semibold dark:text-primary text-wrap"
                  >
                    60 KM de Rennes
                  </p>
                  <p
                    class="mt-1 text-primary font-semibold dark:text-primary text-wrap mb-4"
                  >
                    400 KM de Paris
                  </p>
                  <p class="mt-1 text-gray-500 dark:text-neutral-400 text-wrap">
                    64 rue de la Ville es Cours 35400 Saint Malo
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!--::::::::::::::::::::::::::::::FIN CONTENT::::::::::::::::::::::::::::::::::::::::-->
      </div>
    </div>
  </div>
  <!-- FIN BODY-->
  <div>
    <foot />
  </div>
</template>

<script setup lang="ts">
import sidebar from "./Layout/sidebar.vue";
import Entete from "./Layout/entete.vue";
import foot from "./Layout/foot.vue";
import breadcrumb from "./Layout/breadcrumb.vue";
</script>
