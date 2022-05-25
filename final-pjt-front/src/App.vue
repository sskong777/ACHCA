<template>
  <v-app id="app">
    <nav-bar></nav-bar>

    <router-view></router-view>
    <loading-spinner v-if="!Loading" id="spinner"></loading-spinner>
  </v-app>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import LoadingSpinner from "@/components/LoadingSpinner";
import axios from "axios";

import { mapActions } from "vuex";

export default {
  name: "App",
  components: { NavBar, LoadingSpinner },
  data() {
    return {
      isLoading: false,
    };
  },
  computed: {
    Loading() {
      return this.isLoading;
    },
  },
  methods: {
    ...mapActions(["fetchCurrentUser", "fetchMovies"]),
    setLoading(isLoading) {
      if (isLoading) {
        this.isLoading = true;
      }
      if (!isLoading) {
        this.isLoading = false;
      }
    },
  },
  created() {
    this.fetchCurrentUser();
    axios.interceptors.request.use(
      (config) => {
        this.setLoading(false);

        return config;
      },
      (error) => {
        this.setLoading(false);
        return Promise.reject(error);
      }
    ),
      axios.interceptors.response.use(
        (response) => {
          this.setLoading(true);
          return response;
        },
        (error) => {
          this.setLoading(false);
          return Promise.reject(error);
        }
      );
  },
  mounted() {
    this.fetchMovies();
  },
};
</script>

<style>
@font-face {
  font-family: "GmarketSansBold";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansBold.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "KOTRA_BOLD-Bold";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-10-21@1.1/KOTRA_BOLD-Bold.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
#app {
  background: black;
  color: white;
  font-family: "KOTRA_BOLD-Bold";
  /* font-family: 'GmarketSansBold'; */
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  /* font-family: 'Fredoka One', cursive; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
div img {
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transform: scale(1);
  -webkit-transition: 0.3s;
  -moz-transition: 0.3s;
  -ms-transition: 0.3s;
  -o-transition: 0.3s;
  transition: 0.3s;
}
div img:hover {
  -webkit-transform: scale(1.1);
  -moz-transform: scale(1.1);
  -ms-transform: scale(1.1);
  -o-transform: scale(1.1);
  transform: scale(1.1);
}
#app {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
