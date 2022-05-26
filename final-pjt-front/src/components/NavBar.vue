<template>
  <nav
    class="navbar navbar-expand-xl navbar-dark bg-black sticky-top py-5 stroke fill"
  >
    <!-- <ul> -->
    <div class="container-fluid d-flex justify-content-between">
      <router-link
        :to="{ name: 'movies' }"
        class="navbar-brand text-danger fw-bold"
      >
        <img
          src="https://dewey.tailorbrands.com/production/brand_version_mockup_image/254/7329279254_4f67787a-afe9-4bda-8c74-90a88f6ddf78.png?cb=1653357128
      "
          alt=""
          width="100"
          height="70"
        />
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div
        class="collapse navbar-collapse flex-grow-0"
        id="navbarSupportedContent"
      >
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 d-flex">
          <li class="nav-item me-3">
            <router-link :to="{ name: 'movies' }" class="nav-link">
              Home
            </router-link>
          </li>
          <li v-if="isLoggedIn" class="nav-item me-3">
            <router-link
              :to="{ name: 'movieRecommend', params: { username } }"
              class="nav-link"
              >Recommend</router-link
            >
          </li>
          <li class="nav-item me-3">
            <router-link :to="{ name: 'movieTheater' }" class="nav-link">
              Theater</router-link
            >
          </li>
          <li class="nav-item me-3">
            <router-link :to="{ name: 'articles' }" class="nav-link"
              >Community</router-link
            >
          </li>
          <li v-if="!isLoggedIn" class="nav-item me-3">
            <router-link :to="{ name: 'login' }" class="nav-link"
              >Login</router-link
            >
          </li>
          <li v-if="!isLoggedIn" class="nav-item me-3">
            <router-link :to="{ name: 'signup' }" class="nav-link"
              >Signup</router-link
            >
          </li>
          <li v-if="isLoggedIn" class="nav-item me-3">
            <router-link
              :to="{ name: 'profile', params: { username } }"
              class="nav-link"
            >
              {{ currentUser.username }}'s page
            </router-link>
          </li>
          <li v-if="isLoggedIn">
            <router-link :to="{ name: 'logout' }" class="nav-link"
              >Logout</router-link
            >
          </li>
        </ul>
      </div>
    </div>
    <!-- </ul> -->
  </nav>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "NavBar",
  computed: {
    ...mapGetters(["isLoggedIn", "currentUser"]),
    username() {
      return this.currentUser.username ? this.currentUser.username : "guest";
    },
  },
};
</script>

<style scoped>
/* NAVIGATION */
nav {
  width: 100%;
  margin: 0 auto;
  background: #fff;
  padding: 3%;
  /* box-shadow: 0px 5px 0px #dedede; */
}
nav ul {
  list-style: none;
  text-align: center;
}
nav ul li {
  display: inline-block;
}
nav ul li a {
  display: block;
  padding: 15px;
  text-decoration: none;
  color: #aaa;
  font-weight: 800;
  text-transform: uppercase;
  margin: 0 10px;
  font-size: 1.25rem;
}
nav ul li a,
nav ul li a:after,
nav ul li a:before {
  transition: all 0.5s;
}
nav ul li a:hover {
  color: red;
}

nav a.router-link-exact-active {
  color: crimson;
}

/* fill stroke */
nav.stroke ul li a,
nav.fill ul li a {
  position: relative;
}
nav.stroke ul li a:after,
nav.fill ul li a:after {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
  width: 0%;
  content: ".";
  color: transparent;
  background: crimson;
  height: 5px;
}
nav.stroke ul li a:hover:after {
  width: 100%;
}

nav.fill ul li a {
  transition: all 2s;
}

nav.fill ul li a:after {
  text-align: left;
  content: ".";
  margin: 0;
  opacity: 0;
}
nav.fill ul li a:hover {
  color: crimson;
  z-index: 1;
}
nav.fill ul li a:hover:after {
  z-index: -10;
  animation: fill 1s forwards;
  -webkit-animation: fill 1s forwards;
  -moz-animation: fill 1s forwards;
  opacity: 1;
}

/* SHIFT */
/* nav.shift ul li a {
  
  position:relative;
  z-index: 1;
}
nav.shift ul li a:hover {
  color:white;
}
nav.shift ul li a:after {
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  margin: auto;
  width: 100%;
  height: 100%;
  content: '.';
  color: transparent;
  background:crimson ;
  visibility: none;
  opacity: 0;
  z-index: -1;
}
nav.shift ul li a:hover:after {
  opacity: 1;
  visibility: visible;
  height: 100%;
} */
</style>
