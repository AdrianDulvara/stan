<template>
  <div class="mt-20">
    <div>
      <div class="mx-10 p-2 text-2xl md:text-4xl font-apexm text-center">
        <div>Favourites</div>
        <div class="mt-10">
          <div class="p-4 xl:w-4/5">
            <FavouriteItem
              class="border-b-2 border-gray-200 
                mb-4"
              v-for="item in favourites.items"
              :key="item.product.id"
              :initialItem="item"
              v-on:removeFromFavourites="removeFromFavourites"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import FavouriteItem from "@/components/FavouriteItem.vue";
export default {
  name: "Favourites",
  components: {
    FavouriteItem,
  },
  data() {
    return {
      favourites: {
        items: [],
      },
    };
  },
  methods: {
    removeFromFavourites(item) {
      this.favourites.items = this.favourites.items.filter(
        (i) => i.product.id != item.product.id
      );
    },
  },
  mounted() {
    this.favourites = this.$store.state.favourites;
    document.title = "Favourites | STAN";
  },
};
</script>
