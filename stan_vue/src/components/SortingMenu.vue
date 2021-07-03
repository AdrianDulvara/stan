<template>
  <div class="flex gap-4 mx-10">
    <button class="flex items-center">
      <a class="font-nunito font-semibold px-1">
        Sort By
      </a>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-5 pb-0.5 w-5"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M19 14l-7 7m0 0l-7-7m7 7V3"
        />
      </svg>
    </button>
    <!-- <div>Filters</div> -->
  </div>
</template>

<script>
export default {
  name: "SortingMenu",
};
</script>

<style></style>
