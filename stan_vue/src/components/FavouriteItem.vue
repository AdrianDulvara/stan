<template>
  <div class="">
    <div class="md:flex md:gap-4 justify-between ">
      <div class="md:flex md:gap-4">
        <figure class="mb-2">
          <img :src="item.product.get_thumbnail" class="p-4" />
        </figure>
        <div
          class="font-body uppercase text-left px-2 text-lg md:text-2xl 
       text-gray-900 mt-4"
        >
          <router-link :to="item.product.get_absolute_url">{{
            item.product.name
          }}</router-link>
          <div class="text-left font-apexm text-3xl">
            ${{ item.product.price }}
          </div>
          <div class="text-sm text-gray-500 font-apex md:mt-24 ">
            <button @click="removeFromFavourites(item)">Remove</button>
          </div>
        </div>
      </div>
      <!-- Need to fix addToCart functionality from favourites -->
      <!-- <div class=" text-right  md:text-center mb-4 md:mt-4 mr-6 md:pt-20">
        <AddToCartButton class="p-1 md:p-4" @click="addToCart" />
      </div> -->
    </div>
  </div>
</template>

<script>
import AddToCartButton from "./AddToCartButton.vue";
export default {
  name: "FavouriteItem",
  components: {
    AddToCartButton,
  },
  props: {
    initialItem: Object,
  },
  data() {
    return {
      item: this.initialItem,
      quantity: 1,
    };
  },
  methods: {
    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }
      const item1 = {
        product: this.item,
        quantity: this.quantity,
      };
      this.$store.commit("addToCart", item1);
    },
    updateFavourites() {
      localStorage.setItem(
        "favourites",
        JSON.stringify(this.$store.state.favourites)
      );
    },
    removeFromFavourites(item) {
      this.$emit("removeFromFavourites", item);
      this.updateFavourites();
    },
  },
};
</script>

<style></style>
