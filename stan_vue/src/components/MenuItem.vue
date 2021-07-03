<template>
  <div class="flex items-center justify-between">
    <figure class=" w-14">
      <img :src="item.get_detail_image" class="p-0.5" />
    </figure>
    <router-link :to="item.get_absolute_url" class="text-xs">{{
      item.name
    }}</router-link>
    <div class="text-xs font-apexm">${{ item.price }}</div>
  </div>
</template>

<script>
export default {
  name: "MenuItem",
  data() {
    return {
      item: this.initialItem,
    };
  },
  props: {
    initialItem: Object,
  },
  methods: {
    updateCart() {
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart));
    },
  },
};
</script>

<style></style>
