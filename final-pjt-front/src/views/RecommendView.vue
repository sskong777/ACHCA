<template>
  <div class="mt-5 pt-5">
    <!-- <h1>Recommend</h1>
    <button @click="[recommendMovies(), topPick()]" class="btn btn-success">TOP 10</button>
    <button @click="[recommendMovies(), userPick()]" class="btn btn-success mx-5">User Recommend</button>
    <button @click="[recommendMovies(), likePick()]" class="btn btn-success">Atrraction</button> -->
    <!-- <div v-if="topCheck"> -->
    <!-- <movie-card v-for="movie in recoMovies[0]" :key="movie.pk" :movie="movie">
    </movie-card>
   </div>
       <div v-if="userCheck">
    <movie-card v-for="movie in recoMovies[1]" :key="movie.pk" :movie="movie">
    </movie-card>
   </div>
       <div v-if="likeCheck">
    <movie-card v-for="movie in recoMovies[2]" :key="movie.pk" :movie="movie">
    </movie-card>
  </div> -->

    <h1>TOP 10</h1>

    <carousel-3d
      :disable3d="true"
      :space="365"
      :clickable="false"
      :controls-visible="true"
      :width="400"
      :height="580"
    >
      <slide
        v-for="(movie, idx) in Object.keys(recoMovies[0]).length"
        :key="idx"
        :index="idx"
      >
        <figure>
          <router-link
            :to="{ name: 'movie', params: { moviePk: recoMovies[0][idx].pk } }"
            class="movie_link"
          >
            <img
              :src="`https://image.tmdb.org/t/p/original/${recoMovies[3][idx].poster_path}`"
              alt="..."
            />
          </router-link>
        </figure>
      </slide>
    </carousel-3d>
    <!-- <vue-glide
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 7}, 1100: {perView: 5}, 600: {perView: 3}}"
    >
      <vue-glide-slide
        v-for="recomovie in recoMovies[0]"
        :key="recomovie.pk">
        <RecoMovieCard :recomovie="recomovie"
          />
      </vue-glide-slide>
    </vue-glide> -->

    <hr />

    <h1 class="mt-5 pt-5">User Recommend</h1>
    <carousel-3d
      :disable3d="true"
      :space="365"
      :clickable="false"
      :controls-visible="true"
      :width="400"
      :height="580"
    >
      <slide
        v-for="(movie, idx) in Object.keys(recoMovies[1]).length"
        :key="idx"
        :index="idx"
      >
        <figure>
          <router-link
            :to="{ name: 'movie', params: { moviePk: recoMovies[1][idx].pk } }"
            class="movie_link"
          >
            <img
              :src="`https://image.tmdb.org/t/p/original/${recoMovies[1][idx].poster_path}`"
              alt="..."
            />
          </router-link>
        </figure>
      </slide>
    </carousel-3d>

    <hr />

    <h1 class="mt-5 pt-5">Attraction</h1>
    <carousel-3d
      :disable3d="true"
      :space="365"
      :clickable="false"
      :controls-visible="true"
      :width="400"
      :height="580"
    >
      <slide
        v-for="(movie, idx) in Object.keys(recoMovies[2]).length"
        :key="idx"
        :index="idx"
      >
        <figure>
          <router-link
            :to="{ name: 'movie', params: { moviePk: recoMovies[2][idx].pk } }"
            class="movie_link"
          >
            <img
              :src="`https://image.tmdb.org/t/p/original/${recoMovies[2][idx].poster_path}`"
              alt="..."
            />
          </router-link>
        </figure>
      </slide>
    </carousel-3d>

    <h1 class="mt-5 pt-5">Attraction2</h1>
    <h4>최신 인기 영화(평점순)</h4>
    <carousel-3d
      :disable3d="true"
      :space="365"
      :clickable="false"
      :controls-visible="true"
      :width="400"
      :height="580"
    >
      <slide
        v-for="(movie, idx) in Object.keys(recoMovies[3]).length"
        :key="idx"
        :index="idx"
      >
        <figure>
          <router-link
            :to="{ name: 'movie', params: { moviePk: recoMovies[3][idx].pk } }"
            class="movie_link"
          >
            <img
              :src="`https://image.tmdb.org/t/p/original/${recoMovies[3][idx].poster_path}`"
              alt="..."
            />
          </router-link>
        </figure>
      </slide>
    </carousel-3d>


  <!-- {{recoMovies[3]}} -->
  </div>
</template>

<script>
import { Glide, GlideSlide } from "vue-glide-js";
import { mapActions, mapGetters } from "vuex";
// import MovieCard from '@/components/movie/MovieCard.vue'
// import RecoMovieCard from '@/components/movie/RecoMovieCard.vue'
export default {
  name: "MovieList",
  components: {
    // RecoMovieCard,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide,
  },
  data() {
    return {
      topCheck: false,
      userCheck: false,
      likeCheck: false,
    };
  },
  computed: {
    ...mapGetters(["recoMovies"]),
    checkTop() {
      return this.topCheck;
    },
    checkUser() {
      return this.userCheck;
    },
    checkLike() {
      return this.likeCheck;
    },
  },
  methods: {
    ...mapActions(["recommendMovies"]),
    topPick: function () {
      this.topCheck = !this.topCheck;
      this.userCheck = false;
      this.likeCheck = false;
    },
    userPick: function () {
      this.userCheck = !this.userCheck;
      this.topCheck = false;
      this.likeCheck = false;
    },
    likePick: function () {
      this.likeCheck = !this.likeCheck;
      this.userCheck = false;
      this.topCheck = false;
    },
  },
  created() {
    this.recommendMovies();
  },
};
</script>

<style>
vue-glide-slide {
  padding: 3em;
}
</style>
