<template>
  <div>
    <entete />
  </div>
  <!--FIN HEADER-->
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
          <!-- Breadcrumb -->
          <breadcrumb onglet="Production" page="Recette" />
          <!--::::::::::::::::::::::::::::::CONTENT::::::::::::::::::::::::::::::::::::::::-->
          <div id="list_recette" class="flex flex-col w-full h-full">
            <div id="recette" class="mt-10">
              <div
                id="recette_banner"
                class="w-full pt-5 pl-5 pr-5 h-15 max-w-5/6 flex justify-between items-center rounded-xl border-3 border-gray-200 bg-primary mb"
              >
                <h1
                  class="text-white flex font-bold text-lg uppercase w-64 rounded-sm mb-5"
                >
                  Recette 1
                </h1>
                <button
                  class="text-white flex font-bold text-lg uppercase rounded-sm mb-5 bg-blue-600 pl-2 pr-2 border border-blue-800"
                >
                  Edit
                </button>
              </div>
              <!--bannière sélectionnée-->
              <div
                id="a_recette_banner"
                class="w-full pt-5 pl-5 pr-5 h-20 flex flex-wrap justify-between items-center rounded-t-xl border-l-3 border-r-3 border-t-3 border-gray-200 bg-blue-400 mb"
              >
                <input
                  class="border-1 w-64 border-gray-400 bg-linear-to-b from-gray-200 via-white via-25% to-white to-90% rounded-sm mb-5"
                  type="nom_recette"
                  name="nom_recette"
                  id="nom_recette"
                  required
                />
                <div class="flex">
                  <button
                    class="text-white flex font-bold text-lg uppercase rounded-sm mb-5 bg-red-600 pl-2 pr-2 border border-red-800 mr-5"
                  >
                    Delete
                  </button>
                  <button
                    class="text-white flex font-bold text-lg uppercase rounded-sm mb-5 bg-blue-600 pl-2 pr-2 border border-blue-800 mr-5"
                  >
                    Copy
                  </button>
                  <button
                    class="text-white flex font-bold text-lg uppercase rounded-sm mb-5 bg-green-600 pl-2 pr-2 border border-green-800"
                  >
                    Save
                  </button>
                </div>
              </div>
              <div
                id="recette_pieces"
                class="w-full flex-wrap flex border-l-3 rounded-b- border-r-3 p-5 border-gray-200 bg-white"
              >
                <carte_piece />
                <carte_piece />
                <carte_piece />
                <carte_piece />
                <carte_piece />
                <carte_piece />
              </div>
            </div>
            <!--::::::::::::::::::::::::::::::FIN CONTENT::::::::::::::::::::::::::::::::::::::::-->
          </div>
        </div>
      </div>
    </div>
  </div>
  <div>
    <foot />
  </div>
</template>

<script setup lang="ts">
import carte_piece from "./Layout/carte_piece.vue";
import entete from "./Layout/entete.vue";
import foot from "./Layout/foot.vue";
import sidebar from "./Layout/sidebar.vue";
import breadcrumb from "./Layout/breadcrumb.vue";
</script>
