<template>
  <div v-if="!!favomovie" class="card bg-black" style="width: 13rem">
    <router-link
      :to="{ name: 'movie', params: { moviePk: favomovie.id } }"
      class="movie_link"
    >
      <img :src="posterUrl" class="card-img-top mx-5 my-5" alt="..." />

      <div class="card-body">
        <h5 class="text-center text-white">{{ favomovie.title }}</h5>
        <!-- <p class="card-text">{{ movie.overview }}</p> -->
      </div>
    </router-link>
  </div>

</template>

<script>
// import { mapActions, mapGetters } from 'vuex'

export default {
    name : "FavoriteMovieCard",
    props:{
      favomovie:Object,
    }, 
    data() {
      return {
        // movie_pk: this.movie.pk,
      }
    },
    computed: {
      // ...mapGetters(['movie']),
      posterUrl () {
        return `https://image.tmdb.org/t/p/original/${this.favomovie.poster_path}`
      },
    },
      methods: {
      // ...mapActions(['fetchMovie'])
    },
    created() {
      // this.fetchMovie()
    }
  }
</script>

<style scope>
  .movie_link{
    text-decoration-line:none ;
    color:aliceblue
  }

  #card img{
    padding:3em;
  }


  
</style>