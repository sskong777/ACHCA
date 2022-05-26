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
            <span class="h6 font-weight-light ms-2">{{ payload.title }}</span>
          </v-card-title>

          <v-card-text class="text-h5 font-weight-bold">
            {{ payload.content }}
          </v-card-text>
          <div>
            <div class="d-flex justify-content-between align-items-end">
              <div class="d-flex px-2">
                <v-list-item-avatar color="grey darken-3">
                  <span class="material-icons"> account_circle </span>
                </v-list-item-avatar>
                <v-list-item-title class="text-left mini-txt p-0" width="">
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
                  <div
                    v-if="
                      currentUser.username === review.user.username &&
                      !isEditing
                    "
                  >
                    <button @click="switchIsEditing">Edit</button> |
                    <button @click="deleteReview(payload)">Delete</button>
                  </div></v-list-item-title
                >
              </div>
              <div align="center" justify="end">
                <div class="d-flex me-5 align-items-start">
                  <svg
                    id="star"
                    xmlns="http://www.w3.org/2000/svg"
                    width="1.6rem"
                    fill="currentColor"
                    class="bi bi-star-fill me-1"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"
                    />
                  </svg>
                  <p class="h3">{{ review.rank }}</p>
                </div>
              </div>
            </div>
            <hr />
            <div class="me-2" style="text-align: right; color: grey">
              <span style="font-size: 0.3rem">생성: {{ created_date }}</span>
              <br />
              <span style="font-size: 0.3rem">수정:{{ updated_date }}</span>
            </div>
          </div>
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
            <!-- <v-rating
              v-model="payload.rank"
              color="yellow darken-3"
              background-color="grey darken-1"
              empty-icon="$ratingFull"
              dense
              half-increments
              hover
              large
              required
            ></v-rating> -->
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
import dayjs from "dayjs";

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
    created_date() {
      return dayjs(this.review.created_at).format("MMM D, YYYY h:mm A");
    },
    updated_date() {
      return dayjs(this.review.updated_at).format("MMM D, YYYY h:mm A");
    },
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

#star {
  color: rgba(249, 168, 37);
}
</style>
