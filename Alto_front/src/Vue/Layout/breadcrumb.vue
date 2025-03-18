<template>
  <div id="breadcrumb">
    <ol class="flex items-center whitespace-nowrap mt-10">
      <li class="inline-flex items-center">
        <a
          class="flex items-center text-xl font-semibold uppercase text-primary focus:outline-none dark:text-neutral-500"
          href="#"
        >
          {{ onglet }}
        </a>
        <svg
          class="shrink-0 mx-2 size-4 text-gray-400 dark:text-neutral-600"
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
      </li>
      <li
        class="inline-flex items-center text-xl font-semibold text-primary truncate dark:text-neutral-200"
        aria-current="page"
      >
        {{ page }}
      </li>
    </ol>
  </div>
</template>
<script setup lang="ts">
defineProps<{ onglet: string; page: string }>();
</script>
