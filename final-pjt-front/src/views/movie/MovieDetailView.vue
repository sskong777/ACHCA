<template>
  <div class="parent">
    <div class="d-flex justify-content-center mainVideo">
      <iframe
        v-if="!!movie.video_key"
        :src="`https://www.youtube.com/embed/${movie.video_key}?autoplay=1&mute=1 `"
        title="YouTube video player"
        frameborder="0"
        allowfullscreen
        autoplay
      ></iframe>
    </div>
    <!-- {{ movie }} -->
    <!-- <div style="position: absolute;"> -->
    <p class="text-left h1 m-2">{{ movie.title }}</p>
    <div class="d-flex justify-content-left">
      <div class="d-inline-flex justify-content-left">
        <div class="">
          <div class="justify-content-left">
            <div class="" width="60%">
              <div class="m-2 d-flex">
                <div id="genre_tag" class="">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="2rem"
                    fill="currentColor"
                    class="bi bi-tags-fill"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M2 2a1 1 0 0 1 1-1h4.586a1 1 0 0 1 .707.293l7 7a1 1 0 0 1 0 1.414l-4.586 4.586a1 1 0 0 1-1.414 0l-7-7A1 1 0 0 1 2 6.586V2zm3.5 4a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z"
                    />
                    <path
                      d="M1.293 7.793A1 1 0 0 1 1 7.086V2a1 1 0 0 0-1 1v4.586a1 1 0 0 0 .293.707l7 7a1 1 0 0 0 1.414 0l.043-.043-7.457-7.457z"
                    />
                  </svg>
                  <p class="mini-font h5">Genres :</p>
                </div>
                <div
                  class="mx-1"
                  v-for="genre in movie.genres"
                  :key="genre.name"
                >
                  <p class="genres" style="font-size: 1.75em; color: grey">
                    #{{ genre.name }},
                  </p>
                </div>
              </div>
              <div class="d-flex mx-2 my-3 align-items-start">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="1.3rem"
                  fill="currentColor"
                  class="bi bi-star-fill me-1"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"
                  />
                </svg>
                <p class="h6 pe-3">{{ movie.vote_avg }}</p>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="1.3rem"
                  fill="currentColor"
                  class="bi bi-star-fill me-1"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"
                  />
                </svg>
                <div class="me-2" id="user_rank">
                  <p class="h6">{{ rankAvg }}</p>
                </div>
              </div>
              <!--  -->
              <div class="m-2">
                <div class="d-flex my-5 align-items-start">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="1.5rem"
                    fill="currentColor"
                    class="bi bi-calendar4-week me-2"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM2 2a1 1 0 0 0-1 1v1h14V3a1 1 0 0 0-1-1H2zm13 3H1v9a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V5z"
                    />
                    <path
                      d="M11 7.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm-3 0a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm-2 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm-3 0a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1z"
                    />
                  </svg>
                  <strong
                    ><p class="h6">{{ date }}</p></strong
                  >
                </div>
              </div>
              <!--  -->
              <div class="m-2">
                <div class="d-flex">
                  <p class="h3">DIRECTOR</p>
                </div>
                <div class="d-flex text-align-center">
                  <strong
                    ><p class="h4" style="text-align: center">
                      {{ movie.director }}
                    </p></strong
                  >
                </div>
              </div>
            </div>
            <div class="d-flex my-2 medium-font">
              <v-btn
                class="align-items-start"
                v-if="like"
                @click="favoriteMovie(moviePk)"
                icon
                color="red"
              >
                <v-icon>mdi-heart</v-icon>
              </v-btn>
              <v-btn
                class="align-items-start"
                v-if="!like"
                icon
                color="grey"
                @click="favoriteMovie(moviePk)"
              >
                <v-icon>mdi-heart</v-icon>
              </v-btn>
              <p class="h5" style="display: table-cell">
                {{ favoriteCount }}
              </p>
            </div>
            <!--  -->
          </div>
        </div>
      </div>
    </div>
    <div>
      <!-- </div> -->
    </div>
    <div class="my-3">
      <v-row id="group">
        <v-col cols="12" class="py-2">
          <v-btn-toggle
            dark
            v-model="text"
            tile
            color="deep-purple accent-2"
            group
          >
            <v-btn @click="overviewPick" value="overview"> overview </v-btn>

            <v-btn @click="actorPick" value="actor"> actor </v-btn>

            <v-btn @click="reviewPick" value="review"> review & rate </v-btn>
          </v-btn-toggle>
        </v-col>
      </v-row>
    </div>
    <!-- <router-link
        :to="{ name: 'actorProfile', params: { actorPk: actor.id } }"
      >
  <div class="mt-4">
    <b-card :img-src="tmdbUrl + actor.img_key" img-alt="Card image" img-right>
      <b-card-text>
        {{ actor.actor_name }}
      </b-card-text>
    </b-card>
  </div>
      </router-link> -->
    <div class="container" v-show="actorCheck">
      <div class="row justify-content-center">
        <div
          class="card p-2 col-6 col-md-3 bg-black"
          v-for="(actor, idx) in movie.actors"
          :key="idx"
        >
          <router-link
            class="actor-link"
            :to="{ name: 'actorProfile', params: { actorPk: actor.id } }"
          >
            <div class="card col bg-black" style="width: 18rem">
              <img
                :src="tmdbUrl + actor.img_key"
                class="card-img-top"
                style="border-radius: 30%"
                alt=""
              />
              <div class="card-body">
                <p class="" style="font-size: 1.2rem" id="actorName">
                  {{ actor.actor_name }}
                </p>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </div>
    <!-- <div v-show="actorCheck">
    <div class='d-flex' v-for="(actor, idx) in movie.actors" :key="idx">
      <router-link
        :to="{ name: 'actorProfile', params: { actorPk: actor.id } }"
      >
        <div>
          <img :src="tmdbUrl + actor.img_key" width="100" alt="" />
          {{ actor.actor_name }}
        </div>
      </router-link>
    </div>
  </div> -->
    <div v-show="overviewCheck" class="cols-12 justify-content-center">
      <img
        style="pointer-events: none"
        class="col-12 col-sm-8 col-md-6 col-lg-4"
        :src="posterUrl"
        width="90%"
        alt="..."
      />
      <div class="m-4 col-12 d-flex justify-content-center">
        <p class="lh-lg text-start h6 col-12 col-sm-10">{{ movie.overview }}</p>
      </div>
    </div>

    <!-- Article Edit/Delete UI -->

    <!-- Article Like UI -->

    <hr />
    <!-- Comment UI -->

    <div v-show="reviewCheck">
      <review-list :reviews="movie.reviews"></review-list>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import dayjs from "dayjs";
import ReviewList from "@/components/movie/ReviewList.vue";

export default {
  name: "MovieDetail",
  components: { ReviewList },
  data() {
    return {
      moviePk: this.$route.params.moviePk,
      text: "center",
      overviewCheck: false,
      actorCheck: false,
      reviewCheck: false,
    };
  },
  computed: {
    ...mapGetters(["movie", "currentUser"]),
    checkOverview() {
      return this.overviewCheck;
    },
    checkActor() {
      return this.actorCheck;
    },
    checkReview() {
      return this.reviewCheck;
    },
    favoriteCount() {
      return this.movie.like_users?.length;
    },
    tmdbUrl() {
      return "https://image.tmdb.org/t/p/original";
    },
    posterUrl() {
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`;
    },
    releaseDate() {
      return this.movie.release_date.substr(0, 10);
    },
    like() {
      if (!this.movie.like_users) {
        return false;
      } else if (this.movie.like_users.includes(this.currentUser.pk)) {
        return true;
      } else {
        return false;
      }
    },
    rankAvg() {
      if (!this.movie.reviews?.length) {
        return "no review";
      } else {
        let num = 0;
        this.movie.reviews.forEach(function (review) {
          num += review.rank;
        });
        return (num / this.movie.reviews?.length).toFixed(1);
      }
    },
    date() {
      return dayjs(this.movie.release_date).format("MMMM D, YYYY");
    },
    // makeKey () {
    //   return Object.keys(this.movie.actors)
    //   }
  },

  // movieRank: function () {
  //   return (this.movie.reviews_rank_avg+this.movie.vote_avg)/2
  // }
  methods: {
    ...mapActions(["fetchMovie", "favoriteMovie", "fetchCurrentUser"]),
    overviewPick: function () {
      this.overviewCheck = !this.overviewCheck;
      this.actorCheck = false;
      this.reviewCheck = false;
    },
    actorPick: function () {
      this.actorCheck = !this.actorCheck;
      this.overviewCheck = false;
      this.reviewCheck = false;
    },
    reviewPick: function () {
      this.reviewCheck = !this.reviewCheck;
      this.actorCheck = false;
      this.overviewCheck = false;
    },
  },
  created() {
    this.fetchMovie(this.moviePk);
  },
};
</script>

<style>
.mainVideo {
  margin-top: 20px;
  position: relative;
  width: 100%;
  padding-bottom: 56.25%;
}
.mainVideo iframe {
  position: absolute;
  width: 100%;
  height: 100%;
}

#poster {
  left: 65%;
  width: 30%;
}

#genre_tag {
  color: crimson;
}

#user_rank {
  color: floralwhite;
}

#group {
  background-color: rgb(34, 34, 34);
}

.actor-link {
  text-decoration: none;
}

#actorName {
  color: white;
}

.mini-font {
  font-size: 1.5vw;
}

.medium-font {
  font-size: 2.5vw;
}
</style>
