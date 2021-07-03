<template>
  <div class="mt-20">
    <div class="mt-10">
      <div class="mx-10 p-2 text-2xl md:text-4xl font-apexm text-center">
        <div>My Shopping bag</div>
      </div>

      <div class="xl:flex">
        <div class="p-4 xl:w-2/3">
          <CartItem
            class="border-b-2 border-gray-200"
            v-for="item in cart.items"
            :key="item.product.id"
            :initialItem="item"
            v-on:removeFromCart="removeFromCart"
          />
        </div>
        <div
          v-if="cartTotalLength"
          class=" p-8 xl:fixed right-36 shadow-md rounded-sm"
        >
          <div
            class="text-3xl text-gray-900 
             py-2 px-4 font-apexm mx-10 "
          >
            <div class="border-b-2 p-2 xl:text-4xl">Summary</div>

            <div class="text-xl p-2">Total Items: {{ cartTotalLength }}</div>
            <div class="text-xl p-2 xl:text-3xl">
              Total : ${{ cartTotalPrice }}
            </div>
          </div>
          <div class="text-center mt-6">
            <button
              class="text-white bg-gray-900 text-2xl font-apexm 
            italic py-2 px-5 rounded-full"
            >
              Continue to checkout
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CartItem from "@/components/CartItem.vue";
export default {
  name: "Cart",
  components: {
    CartItem,
  },
  data() {
    return {
      cart: {
        items: [],
      },
    };
  },
  methods: {
    removeFromCart(item) {
      this.cart.items = this.cart.items.filter(
        (i) => i.product.id != item.product.id
      );
    },
  },
  mounted() {
    this.cart = this.$store.state.cart;
    document.title = "My Bag | STAN";
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity);
      }, 0);
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity * curVal.product.price);
      }, 0);
    },
  },
};
</script>

<style></style>
