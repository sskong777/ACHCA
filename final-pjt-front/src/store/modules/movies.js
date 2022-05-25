import axios from "axios";
import drf from "@/api/drf";
import router from "@/router";

import _ from "lodash";
// import accounts from './accounts'
// const api = axios.create({
//   baseURL: "https://api.themoviedb.org/3/",
//   parans: {
//     api_key: "9fd49ab00d660f7801565ddb3d5db886",
//   },
// });
export default {
  // namespaced: true,
  state: {
    movies: [],
    movie: {},
    recoMovies: [],
    reviewAvg: null,
    moviesId: [],
    actorMovies: [],
    actor: {},
  },

  getters: {
    movies: (state) => state.movies,
    movie: (state) => state.movie,
    recoMovies: (state) => state.recoMovies,
    isMovie: (state) => !_.isEmpty(state.movie),
    reviewAvg: (state) => state.reviewAvg,
    moviesId: (state) => state.moviesId,
    actorMovies: (state) => state.actorMovies,
    actor: (state) => state.actor,
  },

  mutations: {
    SET_MOVIES: (state, movies) => (state.movies = movies),
    SET_MOVIE: (state, movie) => (state.movie = movie),
    SET_ACTOR: (state, actor) => (state.actor = actor),
    SET_RECO_MOVIES: (state, recoMovies) => (state.recoMovies = recoMovies),
    SET_MOVIE_REVIEWS: (state, reviews) => (state.movie.reviews = reviews),
    SET_REVIEW_AVG: (state, reviewAvg) => (state.reviewAvg = reviewAvg),
    SET_MOVIES_ID: function (state, movies) {
      movies.forEach(function (movie) {
        state.moviesId.push(movie);
      });
    },
  },

  actions: {
    fetchMovies({ commit }) {
      /* 게시글 목록 받아오기
      GET: articles URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          에러 메시지 표시
      */
      axios
        .get(drf.movies.movies())
        .then(function (res) {
          commit("SET_MOVIES", res.data);
          // commit("SET_MOVIES_ID", res.data);
        })
        .catch((err) => console.error(err.response));
    },
    recommendMovies({ commit }) {
      /* 게시글 목록 받아오기
      GET: articles URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          에러 메시지 표시
      */
      axios
        .get(drf.movies.recommendMovie())
        .then((res) => commit("SET_RECO_MOVIES", res.data))
        .catch((err) => console.error(err.response));
    },

    fetchMovie({ commit }, moviePk) {
      /* 단일 게시글 받아오기
      GET: article URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          단순 에러일 때는
            에러 메시지 표시
          404 에러일 때는
            NotFound404 로 이동
      */
      axios
        .get(drf.movies.movie(moviePk))
        // .then((res) => commit("SET_MOVIE", res.data))
        .then(function (res) {
          commit("SET_MOVIE", res.data);
          commit("SET_REVIEW_AVG", res.data.reviews_rank_avg);
        })
        .catch((err) => {
          console.error(err.response);
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        });
    },

    // createArticle({ commit, getters }, article) {
    //   /* 게시글 생성
    //   POST: articles URL (게시글 입력정보, token)
    //     성공하면
    //       응답으로 받은 게시글을 state.article에 저장
    //       ArticleDetailView 로 이동
    //     실패하면
    //       에러 메시지 표시
    //   */

    //   axios({
    //     url: drf.articles.articles(),
    //     method: "post",
    //     data: article,
    //     headers: getters.authHeader,
    //   }).then((res) => {
    //     commit("SET_ARTICLE", res.data);
    //     router.push({
    //       name: "article",
    //       params: { articlePk: getters.article.pk },
    //     });
    //   });
    // },

    // updateArticle({ commit, getters }, { pk, title, content }) {
    /* 게시글 수정
      PUT: article URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.article에 저장
          ArticleDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
    //   axios({
    //     url: drf.articles.article(pk),
    //     method: "put",
    //     data: { title, content },
    //     headers: getters.authHeader,
    //   }).then((res) => {
    //     commit("SET_ARTICLE", res.data);
    //     router.push({
    //       name: "article",
    //       params: { articlePk: getters.article.pk },
    //     });
    //   });
    // },

    // deleteArticle({ commit, getters }, articlePk) {
    //   /* 게시글 삭제
    //   사용자가 확인을 받고
    //     DELETE: article URL (token)
    //       성공하면
    //         state.article 비우기
    //         AritcleListView로 이동
    //       실패하면
    //         에러 메시지 표시
    //   */

    //   if (confirm("정말 삭제하시겠습니까?")) {
    //     axios({
    //       url: drf.articles.article(articlePk),
    //       method: "delete",
    //       headers: getters.authHeader,
    //     })
    //       .then(() => {
    //         commit("SET_ARTICLE", {});
    //         router.push({ name: "articles" });
    //       })
    //       .catch((err) => console.error(err.response));
    //   }
    // },

    favoriteMovie({ commit, getters }, moviePk) {
      /* 좋아요
      POST: likeArticle URL(token)
        성공하면
          state.article 갱신
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.favoriteMovie(moviePk),
        method: "post",
        headers: getters.authHeader,
      })
        .then((res) => commit("SET_MOVIE", res.data))
        .catch((err) => console.error(err.response));
    },
    followActor({ commit, getters }, actorPk) {
      /* 좋아요
      POST: likeArticle URL(token)
        성공하면
          state.article 갱신
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.followActor(actorPk),
        method: "post",
        headers: getters.authHeader,
      })
        .then((res) => commit("SET_ACTOR", res.data))
        .catch((err) => console.error(err.response));
    },

    createReview({ commit, getters }, { moviePk, title, content, rank }) {
      /* 댓글 생성
      POST: comments URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      const Review = { title, content, rank };

      axios({
        url: drf.movies.reviews(moviePk),
        method: "post",
        data: Review,
        headers: getters.authHeader,
      })
        .then((res) => {
          commit("SET_MOVIE_REVIEWS", res.data);
          console.log(res.data);
        })
        .catch((err) => console.error(err.response));

      axios
        .get(drf.movies.movie(moviePk))
        .then(function (res) {
          commit("SET_REVIEW_AVG", res.data.reviews_rank_avg);
        })
        .catch((err) => {
          console.error(err.response);
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        });
    },

    updateReview(
      { commit, getters },
      { moviePk, reviewPk, title, content, rank }
    ) {
      /* 댓글 수정
      PUT: comment URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      const review = { title, content, rank };

      axios({
        url: drf.movies.review(moviePk, reviewPk),
        method: "put",
        data: review,
        headers: getters.authHeader,
      })
        .then((res) => {
          commit("SET_MOVIE_REVIEWS", res.data);
        })
        .catch((err) => console.error(err.response));
    },

    deleteReview({ commit, getters }, { moviePk, reviewPk }) {
      /* 댓글 삭제
      사용자가 확인을 받고
        DELETE: comment URL (token)
          성공하면
            응답으로 state.article의 comments 갱신
          실패하면
            에러 메시지 표시
      */
      if (confirm("정말 삭제하시겠습니까?")) {
        axios({
          url: drf.movies.review(moviePk, reviewPk),
          method: "delete",
          data: {},
          headers: getters.authHeader,
        })
          .then((res) => {
            console.log(res);
            commit("SET_MOVIE_REVIEWS", res.data);
          })
          .catch((err) => console.error(err.response));
      }
    },

    fetchActor({ commit }, actorPk) {
      /* 단일 게시글 받아오기
      GET: article URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          단순 에러일 때는
            에러 메시지 표시
          404 에러일 때는
            NotFound404 로 이동
      */
      axios
        .get(drf.movies.actor(actorPk))
        // .then((res) => commit("SET_MOVIE", res.data))
        .then(function (res) {
          commit("SET_ACTOR", res.data);
          // commit("SET_REVIEW_AVG", res.data.reviews_rank_avg);
        })
        .catch((err) => {
          console.error(err.response);
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        });
    },
  },
};
