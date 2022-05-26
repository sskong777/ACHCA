<template>
  <div class="container">
    <v-card color="" dark>
      <v-card-title>
        <h1>{{ article.title }}</h1>
      </v-card-title>
      <v-card-text class="text-h5">
        <div v-html="article.content"></div>
      </v-card-text>
      <v-card-text class="py-0">
        <p align="right" class="py-0">
          작성: {{ created_date }}
          <br />
          수정: {{ updated_date }}
        </p>
      </v-card-text>

      <!-- Article Edit/Delete UI -->
      <v-card-actions>
        <div v-if="isAuthor">
          <router-link
            :to="{ name: 'articleEdit', params: { articlePk } }"
            class="text-decoration-none"
          >
            <v-btn color="success" large class="ma-1" plain>
              <v-icon left> mdi-pencil </v-icon>
              Edit
            </v-btn>
          </router-link>

          <!-- <v-btn 
          color = 'red accent-4'
          class="mx-3" 
          @click="deleteArticle(articlePk)"
          >Delete</v-btn> -->
          <v-btn
            @click="deleteArticle(articlePk)"
            class="ma-1"
            color="error"
            plain
          >
            <v-icon left> delete </v-icon>
            Delete
          </v-btn>
        </div>
        <!-- Article Like UI -->
        <v-spacer></v-spacer>
        <div>
          <v-btn icon color="white" @click="likeArticle(articlePk)">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          {{ likeCount }}명이 이 글을 좋아합니다.
        </div>
      </v-card-actions>
    </v-card>

    <hr />
    <!-- Comment UI -->
    <comment-list :comments="article.comments"></comment-list>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import dayjs from "dayjs";
import CommentList from "@/components/community/CommentList.vue";

export default {
  name: "ArticleDetail",
  components: { CommentList },
  data() {
    return {
      articlePk: this.$route.params.articlePk,
    };
  },
  computed: {
    ...mapGetters(["isAuthor", "article"]),
    likeCount() {
      return this.article.like_users?.length;
    },
    created_date() {
      return dayjs(this.article.created_at).format("MMM D, YYYY h:mm A");
    },
    updated_date() {
      return dayjs(this.article.updated_at).format("MMM D, YYYY h:mm A");
    },
  },
  methods: {
    ...mapActions(["fetchArticle", "likeArticle", "deleteArticle"]),
  },
  created() {
    this.fetchArticle(this.articlePk);
  },
};
</script>

<style></style>
