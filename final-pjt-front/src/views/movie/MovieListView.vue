<template>
  <div v-if="!!movies" class="pt-5">
    <h1 class="text-white">Movie</h1>
    <search-bar></search-bar>
    <div class="home row row-cols-4 justify-content-center mt-5">
      <movie-card
        v-for="movie in movies"
        :key="movie.pk"
        :movie="movie"
        class="mb-3 mx-3"
      >
        <!-- 글 이동 링크 (제목) -->
        <!-- <router-link 
        :to="{ name: 'movie', params: {moviePk: movie.pk} }">
        {{ movie.title }}
      </router-link> -->

        <!-- 댓글 개수/좋아요 개수 -->
      </movie-card>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import MovieCard from "@/components/movie/MovieCard.vue";
import SearchBar from "@/components/movie/SearchBar";

export default {
  name: "MovieList",
  components: {
    MovieCard,
    SearchBar,
  },
  computed: {
    ...mapGetters(["movies"]),
  },
  methods: {},
  created() {},
};
</script>

<style></style>
