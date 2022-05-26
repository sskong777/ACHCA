<template>
  <div class="justify-content-center">
    <genres-combo @search-genres="selectGenres"></genres-combo>
    <hr />

    <div class="row row-cols-4 justify-content-center mt-5">
      <movie-card
        v-for="movie in selected_movie"
        :key="movie.pk"
        :movie="movie"
        class="mb-3 mx-3"
      >
      </movie-card>
    </div>
    <div v-if="!check"><p class="h1">장르를 선택해 주세요</p></div>
    <div v-else-if="select_length == 0">
      <p class="h1">없어용~</p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import MovieCard from "@/components/movie/MovieCard.vue";
import GenresCombo from "@/components/movie/GenresCombo";

export default {
  name: "GenresView",
  components: {
    GenresCombo,
    MovieCard,
  },
  data() {
    return {
      selected_movie: [],
      check: false,
    };
  },
  computed: {
    ...mapGetters(["movies"]),
    select_length() {
      return this.selected_movie?.length;
    },
  },
  methods: {
    selectGenres(child) {
      this.check = true;
      const temp_movie = [];
      this.movies.forEach(function (movie) {
        let origin_genre = [];
        movie.genres.forEach(function (genre) {
          origin_genre.push(genre.pk);
        });
        const check = child.filter((x) => !origin_genre.includes(x));
        if (check?.length == 0) {
          temp_movie.push(movie);
        }
      });
      this.selected_movie = temp_movie;
    },
  },
};
</script>

<style></style>
