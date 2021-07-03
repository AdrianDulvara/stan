<template>
  <div class="p-4 mb-2 flex flex-row justify-between">
    <div class="md:flex md:gap-4">
      <figure class="mb-2">
        <img :src="item.product.get_thumbnail" class="p-4" />
      </figure>
      <div
        class="font-body uppercase px-2 text-lg md:text-2xl 
       text-gray-900 mt-4"
      >
        <router-link :to="item.product.get_absolute_url">{{
          item.product.name
        }}</router-link>
      </div>
    </div>
    <div class="md:flex md:gap-4 ">
      <div class="font-apexm italic text-lg md:text-2xl  gap-2 mx-2  p-4">
        <div>
          Quantity
        </div>
        <div class="md:text-center">
          <button @click="decrementQuantity(item)">-</button>
          {{ item.quantity }}
          <button @click="incrementQuantity(item)">+</button>
        </div>
      </div>
      <div class="p-4">
        <div class="font-apexm text-2xl mx-2">
          ${{ getItemTotal(item).toFixed(2) }}
        </div>
        <div class="text-gray-500 mx-2">
          <button @click="removeFromCart(item)">Remove</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CartItem",
  props: {
    initialItem: Object,
  },
  data() {
    return {
      item: this.initialItem,
    };
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price;
    },
    incrementQuantity(item) {
      item.quantity += 1;
      this.updateCart();
    },
    decrementQuantity(item) {
      item.quantity -= 1;
      if (item.quantity === 0) {
        this.$emit("removeFromCart", item);
      }
      this.updateCart();
    },
    updateCart() {
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart));
    },
    removeFromCart(item) {
      this.$emit("removeFromCart", item);
      this.updateCart();
    },
  },
};
</script>

<style></style>
