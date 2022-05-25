<template>
  <div class="container">
    <!-- <img src="https://dewey.tailorbrands.com/production/brand_version_mockup_image/254/7329279254_4f67787a-afe9-4bda-8c74-90a88f6ddf78.png?cb=1653357128
        " alt="" width="300" height="200" class="my-5"> -->

    <div class="box">
      <img class="" src="@/assets/머리탁.png" alt="" />
      <h1 class="text" align="center">앗챠챠 로그인</h1>
    </div>

    <hr />
    <h1>Login</h1>

    <account-error-list v-if="authError"></account-error-list>

    <div class="container" align="left">
      <form @submit.prevent="login(credentials)">
        <div class="form-group">
          <label for="username">Username </label>
          <input
            style="black"
            class="form-control text-black"
            v-model="credentials.username"
            type="text"
            id="username"
            required
            placeholder="Username"
          />
        </div>

        <div class="form-group my-4">
          <label for="password">Password </label>
          <input
            class="form-control"
            v-model="credentials.password"
            type="password"
            id="password"
            required
            placeholder="Password"
          />
        </div>

        <button class="btn btn-primary">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import AccountErrorList from "@/components/AccountErrorList.vue";

export default {
  name: "LoginView",
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: "",
        password: "",
      },
    };
  },
  computed: {
    ...mapGetters(["authError"]),
  },
  methods: {
    ...mapActions(["login"]),
  },
};
</script>

<style scoped>
img {
  max-width: 50%;
  max-height: 50%;
}
.box {
  position: relative;
  transition: 0.5s ease;
}

.text {
  position: absolute;
  visibility: hidden;
}

.box:hover {
  opacity: 0.7;
}

.box:hover .text {
  visibility: visible;
}
</style>
