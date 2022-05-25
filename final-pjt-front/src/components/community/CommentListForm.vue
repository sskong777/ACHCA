<template>
  <div>
    <!-- <form @submit.prevent="onSubmit" class="comment-list-form" > -->
    <v-form>
      <v-text-field
        dark
        label="댓글을 작성하세요."
        hide-details="auto"
        v-model="content"
        color="purple"
        loading
        required
      ></v-text-field>
      <!-- <v-btn large id="btn" @click="onSubmit">댓글 작성</v-btn> -->
      <!-- <p align="right"> -->
      <v-btn class="ma-1" color="purple" plain large @click="onSubmit"
        >댓글 작성</v-btn
      >
      <!-- </p> -->
    </v-form>

    <!-- </form> -->
  </div>
</template>

<script>
// import { VueEditor } from "vue2-editor";

import { mapGetters, mapActions } from "vuex";

export default {
  name: "CommentListForm",
  components: {
    // VueEditor,
  },
  data() {
    return {
      content: "",
    };
  },
  computed: {
    ...mapGetters(["article"]),
  },
  methods: {
    ...mapActions(["createComment"]),
    onSubmit() {
      this.createComment({ articlePk: this.article.pk, content: this.content });
      this.content = "";
    },
  },
};
</script>

<style>
.comment-list-form {
  /* border: 1px solid black; */
  margin: 1rem;
  padding: 1rem;
}
</style>
