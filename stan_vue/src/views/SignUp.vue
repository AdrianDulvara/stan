<template>
  <div class="mt-20 ">
    <div class="flex items-center justify-center">
      <form
        @submit.prevent="submitForm"
        class="text-2xl  p-2 
      font-apexm  m-4"
      >
        <div class="font-apexm text-4xl mb-6 text-center">SIGN-Up</div>
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
          <div class="m-2">
            <label class="block mb-1">Repeat Password </label>
            <input
              type="text"
              v-model="passwordRepeat"
              class="border-2
          font-nunito block"
            />
          </div>
        </div>
        <div class="bg-red-600 text-white p-4" v-if="errors.length">
          <div v-for="error in errors" v-bind:key="error">
            {{ error }}
          </div>
        </div>
        <div class="p-2 text-center ">
          <button
            class="px-4 py-2 rounded-lg 
         text-white bg-red-700"
          >
            Sign up
          </button>
        </div>
        <div
          class="font-sans font-thin
        text-center text-sm mt-4 px-4 pb-2"
        >
          Already have an account?

          <router-link to="/login" class="italic text-red-700 font-apexm">
            Login
          </router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      password: "",
      passwordRepeat: "",
      errors: [],
    };
  },
  methods: {
    submitForm() {
      this.errors = [];
      if (this.username === "") {
        this.errors.push("The username is missing");
      }
      if (this.password === "") {
        this.errors.push("The password is too short");
      }
      if (this.password != this.passwordRepeat) {
        this.errors.push("The passwords doesn't match");
      }
      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
        };
        axios
          .post("/api/v1/users/", formData)
          .then((response) => {
            this.$router.push("/login");
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
              }
              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again");

              console.log(JSON.stringify(error));
            }
          });
      }
    },
  },
};
</script>

<style></style>
