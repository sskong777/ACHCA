const HOST = "http://localhost:8000/api/v1/";

const ACCOUNTS = "accounts/";
const COMMUNITY = "community/";
const COMMENTS = "comments/";
const MOVIES = "movies/";
const REVIEWS = "reviews/";

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + "login/",
    logout: () => HOST + ACCOUNTS + "logout/",
    signup: () => HOST + ACCOUNTS + "signup/",
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + "user/",
    // username으로 프로필 제공
    profile: (username) => HOST + ACCOUNTS + "profile/" + username,
  },
  articles: {
    // /articles/
    articles: () => HOST + COMMUNITY + "articles/",
    // /articles/1/
    article: (articlePk) => HOST + COMMUNITY + "articles/" + `${articlePk}/`,
    likeArticle: (articlePk) =>
      HOST + COMMUNITY + "articles/" + `${articlePk}/` + "like/",
    comments: (articlePk) => HOST + COMMUNITY + COMMENTS + `${articlePk}/`,
    comment: (articlePk, commentPk) =>
      HOST + COMMUNITY + COMMENTS + `${articlePk}/` + `${commentPk}/`,
  },
  movies: {
    // /articles/
    movies: () => HOST + MOVIES,
    // /articles/1/
    movie: (moviePk) => HOST + MOVIES + `${moviePk}/`,
    favoriteMovie: (moviePk) => HOST + MOVIES + `${moviePk}/` + "favorite/",
    recommendMovie: () => HOST + MOVIES + "recommended/",
    reviews: (moviePk) => HOST + MOVIES + `${moviePk}/` + REVIEWS,
    review: (moviePk, reviewPk) =>
      HOST + MOVIES + `${moviePk}/` + REVIEWS + `${reviewPk}/`,
    actor: (actorPk) => HOST + MOVIES + "actor/" + `${actorPk}/`,
    followActor: (actorPk) =>
      HOST + MOVIES + "actor/" + `${actorPk}/` + "follow/",
  },
};
