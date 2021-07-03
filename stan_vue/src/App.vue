<template>
  <!-- wrapper -->
  <div class="py-16">
    <div
      id="nav"
      class=" fixed left-0 right-0 top-0 z-50 h-auto shadow-md md:shadow-none
   px-4 py-4 bg-white text-gray-800 font-body  text-3xl   "
    >
      <div class="flex items-center flex-row gap-4 justify-between  ">
        <div>
          <router-link class="" to="/">
            <Logo />
          </router-link>
        </div>
        <div class="hidden xl:flex">
          <a href="https://github.com/AdrianDulvara">
            <div class="text-2xl italic uppercase text-black font-apexm ml-48">
              <div class="text-3xl inline-block">@</div>
              <div class="inline-block">adi.dulvara</div>
            </div></a
          >
        </div>
        <div class=" hidden md:flex flex-row space-x-2 items-center">
          <SearchBox />
          <div
            class="pt-1.5"
            @mouseover="authOpen = true"
            @mouseleave="authOpen = false"
          >
            <button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-7 w-7"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                />
              </svg>
            </button>
            <div
              v-if="authOpen"
              class="fixed top-14 right-20 z-50
       bg-gray-50 grid
          text-right text-black
    text-lg font-apexm italic p-4 "
            >
              <router-link to="/login">Login</router-link>
              <router-link to="/signup">signup</router-link>
            </div>
          </div>

          <router-link to="/favourites">
            <FavouriteIcon class="mt-0.5" />
            <a
              class="text-xs px-1 rounded-full mr-1
            fixed top-8 font-apexm right-16"
            >
              {{ favouritesTotalLength }}
            </a>
          </router-link>
          <router-link
            to="/cart"
            class="flex items-center "
            @mouseover="cartHover = true"
            @mouseleave="cartHover = false"
            ><svg
              width="34"
              height="28"
              viewBox="0 0 22 28"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <rect
                x="1"
                y="6.5"
                width="20"
                height="20"
                rx="2"
                stroke="#222222"
                stroke-width="2"
              />
              <mask id="path-2-inside-1" fill="white">
                <rect x="4.40002" width="13.2" height="7.7" rx="1" />
              </mask>
              <rect
                x="4.40002"
                width="13.2"
                height="7.7"
                rx="1"
                stroke="#222222"
                stroke-width="4"
                mask="url(#path-2-inside-1)"
              />
            </svg>
            <div class="text-sm font-apex fixed  mt-1 ml-3.5 ">
              {{ cartTotalLength }}
            </div>
            <!-- Cart Menu -->
            <div
              v-if="cartHover"
              class="bg-gray-50 shadow-sm text-sm
               font-apex fixed top-14 right-4"
            >
              <div
                class="font-body text-xs p-2 text-center border-b-2
                border-gray-800"
              >
                My Shopping Bag
              </div>
              <MenuItem
                class="border-b-2"
                v-for="item in cart.items"
                :key="item.product.id"
                :initialItem="item"
              />
            </div>
            <!-- End Cart Menu -->
          </router-link>
        </div>
        <div class="flex items-center gap-2 md:hidden">
          <div class="md:hidden">
            <router-link to="/favourites"> <FavouriteIcon /></router-link>
          </div>
          <div
            class="flex items-center 
           md:hidden"
          >
            <!-- Hambuger Menu Button -->
            <button class="focus:outline-none " @click="isOpen = !isOpen">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-8 w-8"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 6h16M4 12h16M4 18h16"
                />
              </svg>
            </button>
            <!-- Hambuger Menu Button ends -->
          </div>
        </div>
      </div>
    </div>
    <!-- Category menu begins -->
    <div
      class="hidden bg-gray-100 fixed left-0 right-0 mt-3.5 z-40 h-auto
       font-body py-2 text-black 
       md:flex flex-row gap-6 justify-center text-xl italic uppercase"
    >
      <router-link to="/lifestyle">Lifestyle</router-link>
      <router-link to="/fitness">Fitness</router-link>
      <router-link class="text-red-700" to="/onsale"> SALE!</router-link>
    </div>
    <!-- Category menu ends -->

    <!-- Mobile Menu begins -->
    <div
      v-if="isOpen"
      class=" md:hidden shadow-lg bg-gray-50
      fixed left-0 right-0 top-12 mt-4 pt-5  pb-2 px-4 
      drop-shadow-lg grid grid-cols-1 gap-1 text-lg 
      text-gray-900 font-body uppercase "
    >
      <router-link to="/favourites">Favourites </router-link>
      <router-link to="/cart">Cart</router-link>
      <router-link to="/about">About</router-link>
      <router-link class="text-red-700 italic" to="/onsale">Sale!</router-link>
    </div>
    <!-- Mobile Menu ends -->

    <section class="">
      <router-view />
    </section>
    <!-- footer begins -->
    <footer
      class="bg-black font-apexm italic uppercase text-2xl  text-white  h-60 py-4 px-8 my-8"
    >
      <div class="">Copyright (c) 2021</div>
      <div class="">
        <a href="https://github.com/AdrianDulvara">
          <div class="text-2xl italic uppercase  font-apexm">
            <div class="text-3xl inline-block">@</div>
            <div class="inline-block">adi.dulvara</div>
          </div></a
        >
      </div>
    </footer>
    <!-- footer ends -->
  </div>
</template>

<script>
import axios from "axios";
import Logo from "@/components/Logo.vue";
import SearchBox from "@/components/SearchBox.vue";
import FavouriteIcon from "@/components/FavouriteIcon.vue";
import MenuItem from "@/components/MenuItem.vue";
export default {
  components: { Logo, FavouriteIcon, SearchBox, MenuItem },
  data() {
    return {
      isOpen: false,
      authOpen: false,
      cartHover: false,
      cart: {
        items: [],
      },
      favourites: {
        items: [],
      },
      latestProducts: [],
      cartItems: [],
    };
  },
  beforeCreate() {
    this.$store.commit("initializerSore");
    const token = this.$store.state.token;

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token" + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  mounted() {
    this.cart = this.$store.state.cart;
    this.favourites = this.$store.state.favourites;
    this.getLatestProducts();
    this.cartMenu();
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0;
      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity;
      }
      return totalLength;
    },
    favouritesTotalLength() {
      let totalLength = 0;
      for (let i = 0; i < this.favourites.items.length; i++) {
        totalLength++;
      }
      return totalLength;
    },
  },
  methods: {
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
    cartMenu() {
      for (item in this.cart.items) {
        this.cartItems.push(item);
        console.log(this.cart.items);
      }
    },
  },
};
</script>
