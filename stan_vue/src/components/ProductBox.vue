<template>
  <div class="p-4 mb-4 shadow-md flex flex-col items-center">
    <div>
      <figure class="mb-2">
        <img :src="product.get_image" class="p-4" />
      </figure>
      <div class="text-xl text-gray-800 uppercase font-body mx-4">
        <router-link :to="product.get_absolute_url" class="">{{
          product.name
        }}</router-link>
      </div>
      <div class="flex justify-between  items-center">
        <div class="text-gray-800 font-apexm mx-4 text-2xl ">
          ${{ product.price }}
        </div>
        <div class="flex items-center">
          <div class=" text-right  text-gray-700 ">
            <button
              @click="addToFavourites()"
              class="bg-gray-50 rounded-lg p-3 shadow-md"
            >
              <svg
                width="28"
                height="26"
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
          <div
            @click="toggleModal = true"
            class=" text-right p-2 text-gray-700 
          "
          >
            <AddToCartButton @click="addToCart()" />
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
import AddCartModal from "./AddCartModal.vue";
import AddToCartButton from "./AddToCartButton.vue";
export default {
  name: "ProductBox",
  components: {
    AddCartModal,
    AddToCartButton,
  },
  props: {
    product: Object,
  },
  data() {
    return {
      quantity: 1,
      toggleModal: false,
    };
  },

  methods: {
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
