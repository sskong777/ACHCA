<template>
  <div class="container">
    <li class="review-list-item">
      <div v-if="!isEditing">
        <v-card
          class="mx-auto"
          color="
#212121"
          dark
          width="90%"
          row
        >
          <v-card-title>
            <span class="text-h6 font-weight-light ms-2">{{
              payload.title
            }}</span>
          </v-card-title>

          <v-card-text class="text-h5 font-weight-bold">
            {{ payload.content }}
          </v-card-text>

          <v-card-actions>
            <v-list-item>
              <span>
                <v-list-item-avatar color="grey darken-3">
                  <span class="material-icons"> account_circle </span>
                </v-list-item-avatar>
                <v-list-item-title class="text-left mini-txt" width="">
                  <router-link
                    id="username"
                    :to="{
                      name: 'profile',
                      params: { username: review.user.username },
                    }"
                  >
                    <p class="font-weight-light">
                      {{ review.user.username }}
                    </p>
                  </router-link>
                  <span
                    v-if="
                      currentUser.username === review.user.username &&
                      !isEditing
                    "
                  >
                    <button @click="switchIsEditing">Edit</button> |
                    <button @click="deleteReview(payload)">Delete</button>
                  </span></v-list-item-title
                ></span
              >

              <div align="center" justify="end">
                <div class="text-center mt-12 mini-txt">
                  <hr />
                  created: {{ review.created_at }}
                  <br />
                  updated:{{ review.updated_at }}
                  <v-rating
                    :value="payload.rank / 2"
                    color="yellow darken-3"
                    background-color="grey darken-1"
                    empty-icon="$ratingFull"
                    dense
                    half-increments
                    large
                  ></v-rating>
                </div>
              </div>
            </v-list-item>
          </v-card-actions>
        </v-card>
        <hr />
      </div>

      <!-- 수정 중 -->
      <div v-if="isEditing">
        <form @submit.prevent="onSubmit" width="80%" class="review-list-form">
          <div>
            <label for="exampleFormControlInput1" class="form-label"
              >Title</label
            >
            <input
              v-model="payload.title"
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="TITLE"
              required
            />
          </div>
          <div>
            <label for="exampleFormControlTextarea1" class="form-label"
              >Content</label
            >
            <textarea
              v-model="payload.content"
              class="form-control"
              id="exampleFormControlTextarea1"
              rows="3"
              required
            ></textarea>
          </div>
          <div class="text-center mt-12">
            <v-rating
              v-model="payload.rank"
              color="yellow darken-3"
              background-color="grey darken-1"
              empty-icon="$ratingFull"
              dense
              half-increments
              hover
              large
              required
            ></v-rating>
          </div>

          <v-btn rounded @click="onUpdate" dark id="update" class="mt-4 me-1">
            Update Review
          </v-btn>
          <v-btn rounded @click="switchIsEditing" dark class="mt-4">
            cancle
          </v-btn>
        </form>
      </div>
    </li>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ReviewListItem",
  props: { review: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.movie,
        reviewPk: this.review.pk,
        title: this.review.title,
        content: this.review.content,
        rank: this.review.rank,
      },
    };
  },
  computed: {
    ...mapGetters(["currentUser"]),
  },
  methods: {
    ...mapActions(["updateReview", "deleteReview"]),
    switchIsEditing() {
      this.isEditing = !this.isEditing;
    },
    onUpdate() {
      this.updateReview(this.payload);
      this.isEditing = false;
    },
  },
};
</script>

<style scoped>
#username {
  text-decoration-line: none;
  color: azure;
  font-size: 1.2rem;
  text-shadow: cadetblue;
}

.mini-txt {
  font-size: 1.5vw;
}

#update {
  background-color: firebrick;
}
</style>
