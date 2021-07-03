<template>
  <div
    class="shadow-md rounded-md flex gap-4
  py-2 pl-6 pr-12  text-gray-800 font-apexm uppercase bg-white
   duration-200 ease-in-out text-lg items-center"
  >
    <div class="py-1.5">
      <div class="text-sm">
        {{ name }}
      </div>
      was Added to bag
    </div>
  </div>
</template>

<script>
export default {
  name: "AddCartModal",
  props: {
    name: String,
  },
  data() {
    return {};
  },
};
</script>

<style></style>
