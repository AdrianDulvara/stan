<template>
  <div class="bg-gray-100 hover:bg-gray-200 rounded-full px-4">
    <form method="get" action="/search" class="rounded-full">
      <div class="flex flex-row items-center ">
        <button>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5 "
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
        </button>
        <input
          type="text"
          class="bg-gray-100 hover:bg-gray-200 p-2 text-sm font-apex italic  text-gray-800 focus:outline-none w-28"
          placeholder="Search"
          name="query"
        />
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "SearchBox",
};
</script>

<style></style>
