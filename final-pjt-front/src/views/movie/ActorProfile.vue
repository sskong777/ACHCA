<template>
  <div>
    <!-- <h1>{{ '배우 프로필' }}</h1> -->
    <h1>{{ actor.actor_name }} 프로필</h1>
    <hr />
    <h2>출연한 영화</h2>
    <hr />
    <!-- 팔로우 버튼 -->
    <button
      v-if="!follow"
      @click="followActor(actor.id)"
      class="btn btn-outline-danger btn-sm"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="currentColor"
        class="bi bi-emoji-smile"
        viewBox="0 0 16 16"
      >
        <path
          d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"
        />
        <path
          d="M4.285 9.567a.5.5 0 0 1 .683.183A3.498 3.498 0 0 0 8 11.5a3.498 3.498 0 0 0 3.032-1.75.5.5 0 1 1 .866.5A4.498 4.498 0 0 1 8 12.5a4.498 4.498 0 0 1-3.898-2.25.5.5 0 0 1 .183-.683zM7 6.5C7 7.328 6.552 8 6 8s-1-.672-1-1.5S5.448 5 6 5s1 .672 1 1.5zm4 0c0 .828-.448 1.5-1 1.5s-1-.672-1-1.5S9.448 5 10 5s1 .672 1 1.5z"
        />
      </svg>
      Follow
    </button>
    <!-- 언팔로우 버튼 -->
    <button
      v-if="follow"
      @click="followActor(actor.id)"
      class="btn btn-danger btn-sm"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="currentColor"
        class="bi bi-emoji-dizzy"
        viewBox="0 0 16 16"
      >
        <path
          d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"
        />
        <path
          d="M9.146 5.146a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 0 1 .708.708l-.647.646.647.646a.5.5 0 0 1-.708.708l-.646-.647-.646.647a.5.5 0 1 1-.708-.708l.647-.646-.647-.646a.5.5 0 0 1 0-.708zm-5 0a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 1 1 .708.708l-.647.646.647.646a.5.5 0 1 1-.708.708L5.5 7.207l-.646.647a.5.5 0 1 1-.708-.708l.647-.646-.647-.646a.5.5 0 0 1 0-.708zM10 11a2 2 0 1 1-4 0 2 2 0 0 1 4 0z"
        /></svg
      >Unfollow
    </button>

    <!-- {{ actor }} -->

    <!-- 
  <ul>
    <li v-for="(movie, idx) in actor.movies" :key="idx">
      <router-link :to="{ name: 'movie', params: { moviePk: movie.pk } }">
        {{ movie.title }}
      </router-link>
    </li>
  </ul> -->

    <!-- carousel-3d -->
    <carousel-3d
      v-if="!!actor.movies"
      :inverse-scaling="1500"
      :space="800"
      :width="600"
      :height="850"
      :controls-visible="true"
    >
      <slide
        v-for="(movie, idx) in Object.keys(actor.movies).length"
        :key="idx"
        :index="idx"
      >
        <figure>
          <router-link
            :to="{ name: 'movie', params: { moviePk: actor.movies[idx].pk } }"
            class="movie_link"
          >
            <img
              :src="`https://image.tmdb.org/t/p/original/${actor.movies[idx].poster_path}`"
              alt="..."
            />
          </router-link>
        </figure>
      </slide>
    </carousel-3d>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "ActorProfile",
  computed: {
    ...mapGetters(["actor", "currentUser"]),
    follow() {
      if (!this.actor.followed_users) {
        return false;
      } else if (this.actor.followed_users.includes(this.currentUser.pk)) {
        return true;
      } else {
        return false;
      }
    },
  },
  methods: {
    ...mapActions(["fetchActor", "fetchCurrentUser", "followActor"]),
  },
  created() {
    this.fetchActor(this.$route.params.actorPk);
    this.fetchCurrentUser();
  },
};
</script>
