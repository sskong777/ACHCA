<template>
  <div class="container" id="profile">
    <h1 align="left">{{ profile.username }}'s Page</h1>
    <hr />
    <h2>내가 좋아하는 영화</h2>

    <!-- carousel-3d -->
    <carousel-3d
      :controls-visible="true"
      :clickable="false"
      :width="400"
      :height="580"
    >
      <slide
        v-for="(favomovie, idx) in Object.keys(profile.favorite_movies).length"
        :key="idx"
        :index="idx"
      >
        <figure>
          <router-link
            :to="{
              name: 'movie',
              params: { moviePk: profile.favorite_movies[idx].id },
            }"
            class="movie_link"
          >
            <img
              :src="`https://image.tmdb.org/t/p/original/${profile.favorite_movies[idx].poster_path}`"
              alt="..."
            />
          </router-link>
          <!-- <figcaption class="bg-danger text-center">
            {{ profile.favorite_movies[idx].title }}
          </figcaption> -->
        </figure>
      </slide>
    </carousel-3d>
    <hr />
    <!--  -->
    <!--  -->

    <p class="h2">팔로우한 배우</p>
    <v-card width="100%" class="mx-auto">
      <v-container class="pa-1">
        <v-item-group v-model="selected" multiple>
          <div class="row" style="background-color: black">
            <reco-actor-card
              v-for="actor in profile.following_actors"
              :key="actor.pk"
              :actor="actor"
              class=""
            >
            </reco-actor-card>
          </div>
        </v-item-group>
      </v-container>
    </v-card>

    <!--  -->
    <!--  -->
    <hr />
    <h2>내가 작성한 글</h2>

    <carousel-3d
      :perspective="90"
      :controls-visible="true"
      :width="600"
      :display="5"
    >
      <slide
        v-for="(article, i) in profile.articles"
        :key="i"
        :index="i"
        class="bg-dark"
      >
        <v-container class="mx-0">
          <v-row justify="space-around">
            <v-card :width="600">
              <v-img height="25%" src="https://picsum.photos/600/600/?random">
                <v-app-bar flat color="rgba(0, 0, 0, 0)">
                  <v-icon color="grey lighten-1" large> mdi-account </v-icon>
                  <v-toolbar-title class="text-h6 white--text pl-0">
                    {{ article.user.username }}
                  </v-toolbar-title>

                  <v-spacer></v-spacer>

                  <router-link
                    class="text-decoration-none text-white"
                    id="article"
                    :to="{ name: 'article', params: { articlePk: article.pk } }"
                  >
                    <v-btn color="white" icon>
                      <v-icon>article</v-icon>
                    </v-btn>
                  </router-link>
                </v-app-bar>

                <v-card-title class="white--text mt-8">
                  <p>{{ article.title }}</p>
                </v-card-title>
              </v-img>

              <v-card-text>
                <div class="font-weight-bold">
                  {{ article.content }}
                </div>
              </v-card-text>
            </v-card>
          </v-row>
        </v-container>
      </slide>
    </carousel-3d>

    <hr />
    <h2>내가 좋아요 한 글</h2>

    <carousel-3d
      :perspective="180"
      :controls-visible="true"
      :width="600"
      :display="5"
    >
      <slide
        v-for="(article, i) in profile.like_articles"
        :key="i"
        :index="i"
        class="bg-dark"
      >
        <v-container class="mx-0">
          <v-row justify="space-around">
            <v-card>
              <v-img height="25%" src="https://picsum.photos/600/600/?random">
                <v-app-bar flat color="rgba(0, 0, 0, 0)">
                  <v-icon color="grey lighten-1" large> mdi-account </v-icon>
                  <v-toolbar-title class="text-h6 white--text pl-0">
                    {{ article.user.username }}
                  </v-toolbar-title>

                  <v-spacer></v-spacer>

                  <router-link
                    class="text-decoration-none text-white"
                    id="article"
                    :to="{ name: 'article', params: { articlePk: article.pk } }"
                  >
                    <v-btn color="white" icon>
                      <v-icon>article</v-icon>
                    </v-btn>
                  </router-link>
                </v-app-bar>

                <v-card-title class="white--text mt-8">
                  <p>{{ article.title }}</p>
                </v-card-title>
              </v-img>

              <v-card-text>
                <div class="font-weight-bold">
                  {{ article.content }}
                </div>
              </v-card-text>
            </v-card>
          </v-row>
        </v-container>
      </slide>
    </carousel-3d>

    <hr />

    <h2>내가 남긴 리뷰</h2>
    <ul>
      <p v-for="review in profile.reviews" :key="review.pk">
        <router-link
          :to="{ name: 'movie', params: { moviePk: review.movie } }"
          class="movie_link text-white"
        >
          {{ review.title }} ({{ review.rank }}점)
        </router-link>
      </p>
    </ul>
  </div>
</template>

<script>
// import { Glide, GlideSlide } from "vue-glide-js";
import { Carousel3d, Slide } from "vue-carousel-3d";

import { mapGetters, mapActions } from "vuex";
import RecoActorCard from "@/components/movie/RecoActorCard";

// import FavoriteMovieCard from '@/components/movie/FavoriteMovieCard.vue'
// import FavoriteArticle from "@/views/community/FavoriteArticle.vue";

export default {
  name: "ProfileView",
  components: {
    // FavoriteMovieCard,
    // FavoriteArticle,
    // [Glide.name]: Glide,
    // [GlideSlide.name]: GlideSlide,
    Carousel3d,
    Slide,
    RecoActorCard,
  },
  data() {
    return {
      selected: [],
    };
  },
  computed: {
    ...mapGetters(["profile"]),
    // posterUrl () {
    //   return `https://image.tmdb.org/t/p/original/${this.favomovie.poster_path}`
    // },
  },
  methods: {
    ...mapActions(["fetchProfile"]),
  },
  created() {
    const payload = { username: this.$route.params.username };
    this.fetchProfile(payload);
  },
};
</script>

<style scoped></style>
