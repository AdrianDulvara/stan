<template>
  <div class="mt-20">
    <div class="grid md:grid-cols-2">
      <div class="m-4 xl:w-1/2">
        <img :src="product.get_image" class="xl:ml-40" />
      </div>
      <div>
        <div class="xl:w-1/2  p-4">
          <div class="font-body uppercase italic text-2xl px-4 mb-2">
            {{ product.name }}
          </div>
          <div class="font-extralight uppercase  text-sm mb-2 px-4">
            {{ product.description }}
          </div>

          <div
            class="uppercase text-2xl mt-4  font-apexm italic 
            px-4    text-gray-900"
          >
            <div class="font-apex inline-block">Price:</div>
            <div class="inline-block mx-2">${{ product.price }}</div>
          </div>
          <div class="mt-6">
            <div class="px-4 flex items-center text-center">
              <input
                type="number"
                class="border-2 w-16  font-body
                mb-4 focus:outline-none border-gray-900
                 rounded-full 
                 text-gray-900 text-center text-lg py-1 md:pl-4"
                min="1"
                v-model="quantity"
              />
            </div>
            <div
              @click="toggleModal = true"
              class="bg-black text-center rounded-full mx-4"
            >
              <button
                @click="addToCart"
                class="rounded-full text-white 
                focus:outline-none text-xl p-4  font-thin"
              >
                Add to bag
              </button>
            </div>
            <div
              class="bg-white text-center rounded-full  border-2 border-black my-4 mx-4"
            >
              <button
                @click="addToFavourites()"
                class="rounded-full  text-center text-black  focus:outline-none text-xl p-4  font-thin"
              >
                <div class="inline-block">Favourite</div>

                <svg
                  class="inline-block mx-1"
                  width="26"
                  height="25"
                  viewBox="0 0 31 30"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M26.9183 5.76249C26.2586 5.12375 25.4753 4.61705 24.6132 4.27135C23.751 3.92565 22.827 3.74771 21.8938 3.74771C20.9605 3.74771 20.0365 3.92565 19.1743 4.27135C18.3122 4.61705 17.5289 5.12375 16.8692 5.76249L15.5 7.08749L14.1308 5.76249C12.7982 4.47288 10.9908 3.74838 9.10626 3.74838C7.22168 3.74838 5.41428 4.47288 4.08168 5.76249C2.74908 7.05211 2.00043 8.8012 2.00043 10.625C2.00043 12.4488 2.74908 14.1979 4.08168 15.4875L5.45084 16.8125L15.5 26.5375L25.5492 16.8125L26.9183 15.4875C27.5784 14.849 28.102 14.091 28.4592 13.2567C28.8164 12.4224 29.0003 11.5281 29.0003 10.625C29.0003 9.72188 28.8164 8.82762 28.4592 7.9933C28.102 7.15897 27.5784 6.40094 26.9183 5.76249V5.76249Z"
                    stroke="#222222"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      v-if="toggleModal"
      class="fixed bottom-10 right-10 z-50 duration-1000 ease-in"
    >
      <AddCartModal :name="product.name" />
      <button @click="toggleModal = false" class="fixed bottom-16 right-14">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-5 w-5"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fill-rule="evenodd"
            d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
            clip-rule="evenodd"
          />
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import AddCartModal from "@/components/AddCartModal.vue";

export default {
  name: "Product",
  components: { AddCartModal },
  data() {
    return {
      product: {},
      quantity: 1,
      toggleModal: false,
    };
  },
  mounted() {
    this.getProduct();
  },
  methods: {
    async getProduct() {
      const category_slug = this.$route.params.category_slug;
      const product_slug = this.$route.params.product_slug;
      await axios
        .get(`/api/v1/products/${category_slug}/${product_slug}`)
        .then((response) => {
          this.product = response.data;
          document.title = this.product.name + " | STAN";
        })
        .catch((error) => {
          console.log(error);
        });
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }
      const item = {
        product: this.product,
        quantity: this.quantity,
      };
      this.$store.commit("addToCart", item);
    },
    addToFavourites() {
      const item = {
        product: this.product,
        quantity: this.quantity,
      };
      this.$store.commit("addToFavourites", item);
    },
  },
};
</script>

<style></style>
