<template>
  <div class="mt-16 py-4">
    <div>
      <div class="text-4xl p-4 mx-10 font-apexm">
        you have searched : "{{ query }}"
      </div>
    </div>
    <div class="grid md:grid-cols-2 xl:grid-cols-3">
      <ProductBox
        v-for="product in products"
        :key="product.id"
        :product="product"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProductBox from "@/components/ProductBox.vue";
export default {
  name: "Search",
  components: { ProductBox },
  data() {
    return {
      products: [],
      query: "",
    };
  },
  mounted() {
    document.title = "Search | STAN";
    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);
    if (params.get("query")) {
      this.query = params.get("query");
      this.performSearch();
    }
  },
  methods: {
    async performSearch() {
      await axios
        .post("/api/v1/products/search/", { query: this.query })
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          consolge.log(error);
        });
    },
  },
};
</script>
