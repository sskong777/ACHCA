<template>
  <div id="infinite-list" class="pt-5">
    <h1 class="text-white" id="top">Movie</h1>
    <search-bar></search-bar>
    <router-link :to="{ name: 'genre' }" class="movie_link">
      <v-icon dark> mdi-plus </v-icon>
      <p class="h5" style="color: crimson">Go genres</p>
    </router-link>
    <div class="home row row-cols-4 justify-content-center mt-5">
      <movie-card
        v-for="movie in movs"
        :key="movie.id"
        :movie="movie"
        class="mb-3 mx-3"
      >
      </movie-card>
    </div>
    <v-fab-transition>
      <v-btn
        color="red darken-3"
        dark
        fab
        fixed
        bottom
        right
        @click="$vuetify.goTo('#top', { duration: 500, offset: 0 })"
      >
        <v-icon large>mdi-menu-up</v-icon>
      </v-btn>
    </v-fab-transition>
  </div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/scrollmonitor/1.2.0/scrollMonitor.js"></script>
<script>
import { mapGetters } from "vuex";
import axios from "axios";
import MovieCard from "@/components/movie/MovieCard.vue";
import SearchBar from "@/components/movie/SearchBar";

export default {
  name: "MovieList",
  data() {
    return {
      movs: [],
      currentPage: 0,
      hasNext: true,
      scrolledToBottom: false,
    };
  },

  components: {
    MovieCard,
    SearchBar,
  },
  computed: {
    ...mapGetters(["movies"]),
  },
  methods: {
    getMovies() {
      this.currentPage += 1;
      if (this.currentPage == 41) {
        this.currentPage = 1;
      }
      axios
        .get(
          `${process.env.VUE_APP_SERVER_URL}get_movies/?page=${this.currentPage}`
        )
        .then((response) => {
          return response.data;
        })
        .then((data) => {
          // console.log(data.next);
          this.hasNext = false;
          if (data.next) {
            this.hasNext = true;
          }
          for (let i = 0; i < data.results.length; i++) {
            this.movs.push(data.results[i]);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    scroll() {
      window.onscroll = () => {
        let bottomOfWindow =
          Math.max(
            window.pageYOffset,
            document.documentElement.scrollTop,
            document.body.scrollTop
          ) +
            window.innerHeight >
          document.documentElement.offsetHeight;

        if (bottomOfWindow) {
          this.scrolledToBottom = true; // replace it with your code
          this.getMovies();
        }
      };
    },
  },
  mounted() {
    this.getMovies();
    this.scroll();
  },
};
</script>

<style></style>
