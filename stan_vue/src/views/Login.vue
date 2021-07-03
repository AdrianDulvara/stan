<template>
  <div class="mt-20 ">
    <div class="flex items-center justify-center">
      <form
        @submit.prevent="submitForm"
        class="text-2xl  p-2 
      font-apexm  m-4"
      >
        <div class="font-apexm text-4xl mb-6 text-center">Login</div>
        <div class="p-2">
          <div class="m-2">
            <label class="block mb-1">Username </label>
            <input
              type="text"
              v-model="username"
              class="border-2 block
           font-nunito"
            />
          </div>
          <div class="m-2">
            <label class="block mb-1">Password </label>
            <input
              type="text"
              v-model="password"
              class="border-2
          font-nunito block"
            />
          </div>
        </div>
        <div class="p-2 text-center ">
          <button
            class="px-4 py-2 rounded-lg 
         text-white bg-gray-800"
          >
            Login
          </button>
        </div>
        <div
          class="font-sans font-thin
        text-center text-sm mt-4 px-4 pb-2"
        >
          Don't have an accout?

          <router-link to="/signup" class="italic text-red-700 font-apexm">
            Sign up
          </router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Log In | Djackets";
  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      const formData = {
        username: this.username,
        password: this.password,
      };
      await axios
        .post("/api/v1/token/login/", formData)
        .then((response) => {
          const token = response.data.auth_token;
          this.$store.commit("setToken", token);

          axios.defaults.headers.common["Authorization"] = "Token " + token;
          localStorage.setItem("token", token);
          const toPath = this.$route.query.to || "/cart";
          this.$router.push(toPath);
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }
          } else {
            this.errors.push("Something went wrong. Please try again");

            console.log(JSON.stringify(error));
          }
        });
    },
  },
};
</script>
