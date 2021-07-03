<template>
  <div class="mt-20">
    <section>
      <div class="text-black mb-6 flex items-center justify-between ">
        <div
          class="text-4xl font-semibold px-4 text-center font-apexm uppercase"
        >
          Sneakers
        </div>
        <div @mouseover="sortHover = true" @mouseleave="sortHover = false">
          <SortingMenu />
          <div
            v-if="sortHover"
            class="bg-gray-50 font-apexm italic text-sm
          py-2 px-4 fixed"
          >
            <button class="mb-2" @click="sortBy('price', 'ascending')">
              Price Ascending
            </button>
            <button class="" @click="sortBy('price', 'descending')">
              Price Descending
            </button>
          </div>
        </div>
      </div>
    </section>
    <div class="grid  grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5 mx-4">
      <ProductBox
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProductBox from "@/components/ProductBox.vue";
import AddCartModal from "@/components/AddCartModal.vue";
import SortingMenu from "@/components/SortingMenu.vue";
export default {
  name: "Home",
  components: { ProductBox, AddCartModal, SortingMenu },
  data() {
    return {
      latestProducts: [],
      toggleModal: false,
      sortHover: false,
    };
  },
  mounted() {
    this.getLatestProducts();
    document.title = "Welcome | STAN";
  },
  methods: {
    sortBy(prop, way) {
      if (prop === "price") {
        if (way === "ascending") {
          this.latestProducts.sort(function(a, b) {
            return a[prop] - b[prop];
          });
        } else if (way === "descending") {
          this.latestProducts.sort(function(a, b) {
            return b[prop] - a[prop];
          });
        }
      }
    },

    getLatestProducts() {
      axios
        .get("/api/v1/homepage-products/")
        .then((response) => {
          this.latestProducts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
