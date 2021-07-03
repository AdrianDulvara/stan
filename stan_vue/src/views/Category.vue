<template>
  <div class="mt-4 pt-16">
    <section>
      <div class="text-black mb-6 text-center mt-2 ">
        <div class="text-4xl font-semibold px-4 font-apexm uppercase">
          {{ category.name }} footwear
        </div>
      </div>
    </section>
    <div class="grid  grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5 mx-4">
      <ProductBox
        v-for="product in category.products"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProductBox from "@/components/ProductBox.vue";
export default {
  name: "Category",
  components: {
    ProductBox,
  },
  data() {
    return {
      category: {
        products: [],
      },
    };
  },
  mounted() {
    this.getCategory();
  },
  watch: {
    $route(to, from) {
      if (to.name === "Category") {
        this.getCategory();
      }
    },
  },
  methods: {
    getCategory() {
      const categorySlug = this.$route.params.category_slug;
      axios
        .get(`api/v1/products/${categorySlug}/`)
        .then((response) => {
          this.category = response.data;
          document.title = this.category.name + " | STAN ";
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style></style>
