<template>
  <div>
    <Entete />
  </div>

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
          <breadcrumb onglet="Général" page="Guide" />
          <!-- FIN BREADCRUMB-->
          <!--::::::::::::::::::::::::::::::CONTENT::::::::::::::::::::::::::::::::::::::::-->
          <!--STEPPER-->
          <div
            class="flex justify-around flex-wrap-reverse items-center w-full mt-10"
          >
            <div class="container mx-auto p-6">
              <div class="border-2 border-gray-300 p-4 rounded-lg">
                <div class="justify-center flex m-4">
                  <h2 class="text-2xl font-bold text-gray-800 dark:text-white">
                    Création Recette
                  </h2>
                </div>

                <!-- Stepper Navigation -->
                <ul class="relative flex gap-x-10 justify-center w-full">
                  <li
                    v-for="(step, index) in steps"
                    :key="step.index"
                    :class="{
                      'text-blue-600': currentStep === step.index,
                      'text-gray-400': currentStep !== step.index,
                    }"
                    class="flex items-center gap-x-2 group cursor-pointer"
                    @click="goToStep(index)"
                  >
                    <span
                      class="min-w-7 min-h-7 flex justify-center items-center text-xs font-medium rounded-full bg-gray-100 group-focus:bg-blue-600"
                      :class="{
                        'bg-blue-600 text-white': currentStep > step.index,
                        'bg-gray-200': currentStep <= step.index,
                      }"
                    >
                      <span v-if="currentStep > step.index" class="text-white"
                        >✔</span
                      >
                      <span v-else>{{ step.index + 1 }}</span>
                    </span>
                    <span class="text-sm font-medium text-gray-800">{{
                      step.name
                    }}</span>
                    <div
                      class="w-full h-px flex-1 bg-gray-200 group-last:hidden"
                      :class="{
                        'bg-blue-600': currentStep > step.index,
                        'bg-gray-200': currentStep <= step.index,
                      }"
                    ></div>
                  </li>
                </ul>

                <!-- Stepper Content -->
                <div class="mt-5">
                  <div
                    v-for="(step, index) in steps"
                    :key="step.index"
                    v-show="currentStep === index"
                  >
                    <div
                      class="p-4 h-48 bg-gray-50 flex justify-center items-center border border-dashed border-gray-200 rounded-xl dark:bg-neutral-800 dark:border-neutral-700"
                    >
                      <h3 class="text-gray-500 dark:text-neutral-500">
                        {{ step.content }}
                      </h3>
                    </div>
                  </div>
                </div>

                <!-- Navigation Buttons -->
                <div class="mt-5 flex justify-between items-center gap-x-2">
                  <button
                    v-if="currentStep > 0"
                    @click="goToStep(currentStep - 1)"
                    class="py-2 px-3 inline-flex items-center gap-x-1 text-sm font-medium rounded-lg border border-gray-200 bg-white text-gray-800 hover:bg-gray-50 dark:bg-neutral-800 dark:text-neutral-300 dark:hover:bg-neutral-700"
                  >
                    <svg
                      class="shrink-0"
                      xmlns="http://www.w3.org/2000/svg"
                      width="24"
                      height="24"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    >
                      <path d="m15 18-6-6 6-6"></path>
                    </svg>
                    Back
                  </button>

                  <button
                    v-if="currentStep < steps.length - 1"
                    @click="goToStep(currentStep + 1)"
                    class="py-2 px-3 inline-flex items-center gap-x-1 text-sm font-medium rounded-lg border border-transparent bg-primary text-white hover:bg-blue-700"
                  >
                    Next
                    <svg
                      class="shrink-0"
                      xmlns="http://www.w3.org/2000/svg"
                      width="24"
                      height="24"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    >
                      <path d="m9 18 6-6-6-6"></path>
                    </svg>
                  </button>
                </div>
              </div>
              <!--DIVSEURR 1 :  CARTES-->
              <div class="flex justify-center w-full mt-4">
                <hr class="hr sm:w-1/2 lg:w-2/3 xl:w-full mt-10" />
              </div>
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
                    Some quick example text to build on the card title and make
                    up the bulk of the card's content.
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
                    Some quick example text to build on the card title and make
                    up the bulk of the card's content.
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
            </div>
          </div>
        </div>
        <!--::::::::::::::::::::::::::::::FIN CONTENT::::::::::::::::::::::::::::::::::::::::-->
      </div>
    </div>
  </div>

  <div>
    <foot />
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

// Définition du type Step
interface Step {
  index: number;
  name: string;
  content: string;
}

// Définition des étapes du stepper
const steps: Step[] = [
  { index: 0, name: "Step 1", content: "Content of Step 1" },
  { index: 1, name: "Step 2", content: "Content of Step 2" },
  { index: 2, name: "Step 3", content: "Content of Step 3" },
];

// Variable pour suivre l'étape courante
const currentStep = ref(0);

// Fonction pour passer à une étape spécifique
const goToStep = (index: number) => {
  currentStep.value = index;
};
import breadcrumb from "./Layout/breadcrumb.vue";
import Entete from "./Layout/entete.vue";
import foot from "./Layout/foot.vue";
import sidebar from "./Layout/sidebar.vue";
</script>
