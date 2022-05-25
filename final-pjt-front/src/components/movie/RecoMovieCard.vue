<template>
  <div class="card bg-black" style="width: 18rem">
    <router-link
      :to="{ name: 'movie', params: { moviePk: recomovie.id } }"
      class="movie_link"
    >
      <img :src="posterUrl" class="card-img-top mx-5 my-5" alt="..." />
      <div class="card-body">
        <h5 class="text-center text-white">{{ recomovie.title }}</h5>
        <!-- <p class="card-text">{{ movie.overview }}</p> -->
      </div>
    </router-link>
  </div>
</template>

<script>
// import { mapActions, mapGetters } from 'vuex'

export default {
  name: "RecoMovieCard",
  props: {
    recomovie: Object,
  },
  data() {
    return {
      // movie_pk: this.movie.pk,
    };
  },
  computed: {
    // ...mapGetters(['movie']),
    posterUrl() {
      return `https://image.tmdb.org/t/p/original/${this.recomovie.poster_path}`;
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

<style scope>
.movie_link {
  text-decoration-line: none;
  color: aliceblue;
}

#card img {
  padding: 3em;
}
</style>
