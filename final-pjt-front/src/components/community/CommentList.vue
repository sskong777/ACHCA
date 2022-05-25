<template>
  <div class="comment-list">
    <p align="left">
      <comment-list-item
        v-for="comment in comments"
        :comment="comment"
        :key="comment.pk"
      >
      </comment-list-item>
    </p>

    <comment-list-form></comment-list-form>
  </div>
</template>

<script>
import CommentListItem from "@/components/community/CommentListItem.vue";
import CommentListForm from "@/components/community/CommentListForm.vue";
// import { mapGetters, mapActions } from 'vuex'

export default {
  name: "CommentList",
  components: { CommentListForm, CommentListItem },
  props: { comments: Array },
};
</script>

<style>
/* .comment-list {
  border: 1px solid blue; */
/* } */
</style>
