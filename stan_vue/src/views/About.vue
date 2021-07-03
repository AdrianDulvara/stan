<template>
  <div class="mt-20 bg-gray-200">
    <div>
      <span @mouseover="hover = true" @mouseleave="hover = false">
        Hover me to show the message!
      </span>
      <span v-if="hover">This is a secret message.</span>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      hover: false,
    };
  },
};
</script>
