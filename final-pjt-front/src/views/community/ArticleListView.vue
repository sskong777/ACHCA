<template v-slot:default>
  <div>
    <img
      src="https://dewey.tailorbrands.com/production/brand_version_mockup_image/254/7329279254_4f67787a-afe9-4bda-8c74-90a88f6ddf78.png?cb=1653357128
      "
      alt=""
      width="300"
      height="200"
      class="my-5"
    />
    <hr />
    <h1>Community</h1>

    <div class="container" align="right">
      <p v-if="isLoggedIn">
        <router-link
          class="text-decoration-none text-white"
          :to="{ name: 'articleNew' }"
        >
          <v-btn class="mx-2" fab dark large color="cyan">
            <v-icon dark> mdi-pencil </v-icon>
          </v-btn>
        </router-link>

        <!-- <router-link class='btn btn-info btn-lg text-decoration-none text-white'
          :to="{ name: 'articleNew' }">
        </router-link> -->
      </p>
      <v-simple-table fixed-header dark>
        <template v-slot:default>
          <thead>
            <tr>
              <th scope="col">번호</th>
              <th scope="col">제목</th>
              <th scope="col">작성자</th>
              <th scope="col">댓글 / 좋아요</th>
            </tr>
          </thead>

          <tbody align="left">
            <tr v-for="(article, idx) in articles" :key="idx">
              <!-- 게시글 번호 -->
              <td>{{ idx + 1 }}</td>

              <!-- 글 이동 링크 (제목) -->
              <td>
                <router-link
                  class="text-decoration-none text-white"
                  :to="{ name: 'article', params: { articlePk: article.pk } }"
                >
                  {{ article.title }}
                </router-link>
              </td>

              <!-- 작성자 -->
              <td>
                <router-link
                  :to="{
                    name: 'profile',
                    params: { username: article.user.username },
                  }"
                  class="fw-bold text-decoration-none text-white"
                >
                  {{ article.user.username }}
                </router-link>
              </td>
              <!-- 댓글 개수/좋아요 개수 -->
              <td>{{ article.comment_count }} / {{ article.like_count }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
      <v-pagination
      
      ></v-pagination>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "ArticleList",
  computed: {
    ...mapGetters(["articles", "isLoggedIn"]),
  },
  methods: {
    ...mapActions(["fetchArticles"]),
  },
  created() {
    this.fetchArticles();
  },
};
</script>

<style></style>
