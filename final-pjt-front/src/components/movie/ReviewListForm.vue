<template>
  <div class="container">
    <form @submit.prevent="onSubmit" width="80%" class="review-list-form">
      <div align="left">
        <label for="exampleFormControlInput1" class="form-label">Title</label>
        <input
          v-model="title"
          type="text"
          class="form-control"
          id="exampleFormControlInput1"
          placeholder="TITLE"
          required
        />
      </div>
      <div align="left" class="my-10">
        <label for="exampleFormControlTextarea1" class="form-label"
          >Content</label
        >
        <textarea
          v-model="content"
          class="form-control"
          id="exampleFormControlTextarea1"
          rows="3"
          placeholder="CONTENT"
          required
        ></textarea>
      </div>
      <div class="text-center mt-12">
        <v-rating
          v-model="rank"
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

      <v-btn rounded dark type="submit" class="mt-4"> Create Review </v-btn>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ReviewListForm",
  data() {
    return {
      title: "",
      content: "",
      rank: 0,
    };
  },
  computed: {
    ...mapGetters(["movie"]),
  },
  methods: {
    ...mapActions(["createReview"]),
    onSubmit() {
      this.createReview({
        moviePk: this.movie.id,
        title: this.title,
        content: this.content,
        rank: this.rank * 2,
      });
      this.content = "";
      this.title = "";
      this.rank = 0;
    },
  },
};
</script>

<style>
.review-list-form {
  border: 1px solid black;
  margin: 1rem;
  padding: 1rem;
}
</style>
