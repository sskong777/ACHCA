<template>
  <div class="card bg-black" style="width: 18rem">
    <router-link
      :to="{ name: 'movie', params: { moviePk: movie.pk } }"
      class="movie_link"
      style="color: white"
    >
      <img :src="posterUrl" class="card-img-top" alt="..." />
      <div class="card-body">
        <h3 class="">{{ movie.title }}</h3>
        <!-- <p class="card-text">{{ movie.overview }}</p> -->
      </div>
    </router-link>
  </div>
</template>

<script>
// import { mapActions, mapGetters } from 'vuex'

export default {
  name: "MovieCard",
  props: {
    movie: Object,
  },
  data() {
    return {
      // movie_pk: this.movie.pk,
    };
  },
  computed: {
    // ...mapGetters(['movie']),
    posterUrl() {
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`;
    },
    go_deail() {
      return `/movies/${this.movie.pk}`;
    },
  },
  methods: {
    // ...mapActions(['fetchMovie'])
  },
  created() {
    // this.fetchMovie()
  },
};
</script>

<style>
.movie_link {
  text-decoration-line: none;
}
</style>
