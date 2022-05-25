<template>
  <div class="comment-list-item">
    <router-link
      :to="{ name: 'profile', params: { username: comment.user.username } }"
      class="fw-bold text-decoration-none text-white"
    >
      {{ comment.user.username }}
    </router-link>
    <p class="text-muted" v-html="payload.content" v-if="!isEditing"></p>

    <!-- 생성: {{ comment.created_at }} / 수정: {{ comment.updated_at }} -->
    <span v-if="isEditing">
      <!-- <input class="bg-white" type="text" v-model="payload.content"> -->
      <!-- <v-input dark >input</v-input> -->
      <v-text-field
        dark
        label="댓글을 수정하세요."
        hide-details="auto"
        v-model="payload.content"
        color="success"
        loading

      ></v-text-field>

      <!-- <v-text-field
        color="success"
        loading
        disabled
      ></v-text-field> -->
      <p align="right">
        <v-btn class="ma-1" color="primary" plain @click="onUpdate">
          Update
        </v-btn>

        <v-btn class="ma-2" color="red" plain large @click="switchIsEditing">
          Cancle
        </v-btn>
      </p>
    </span>

    <p
      v-if="currentUser.username === comment.user.username && !isEditing"
      align="right"
    >
      <!-- <v-btn 
      text
      color = "white"
      @click="switchIsEditing">Edit</v-btn> -->

      <v-btn color="success" large class="ma-1" plain @click="switchIsEditing">
        <v-icon left> mdi-pencil </v-icon>
        Edit
      </v-btn>

      <v-btn @click="deleteComment(payload)" class="ma-1" color="error" plain>
        <v-icon left> delete </v-icon>
        Delete
      </v-btn>
    </p>
    <hr />
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "CommentListItem",
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content,
      },
    };
  },
  computed: {
    ...mapGetters(["currentUser"]),
  },
  methods: {
    ...mapActions(["updateComment", "deleteComment"]),
    switchIsEditing() {
      this.isEditing = !this.isEditing;
    },
    onUpdate() {
      this.updateComment(this.payload);
      this.isEditing = false;
    },
  },
};
</script>

<style>
/* .comment-list-item {
  border: 1px solid green;

} */
</style>
