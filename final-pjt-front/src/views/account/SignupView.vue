<template>
  <div class="container">
    <!-- <img src="https://dewey.tailorbrands.com/production/brand_version_mockup_image/254/7329279254_4f67787a-afe9-4bda-8c74-90a88f6ddf78.png?cb=1653357128
      " alt="" width="300" height="200" class="my-5"> -->

    <div class="box" align="center">
      <img class="" src="@/assets/머리탁.png" alt="" />
      <h1 class="text">앗챠챠 회원가입</h1>
    </div>
    <hr />
    <h1>Signup</h1>

    <account-error-list v-if="authError"></account-error-list>

    <div class="container" align="left">
      <form @submit.prevent="signup(credentials)">
        <div class="form-group">
          <label for="username">Username </label>
          <input
            class="form-control text-black"
            v-model="credentials.username"
            type="text"
            id="username"
            required
            placeholder="Username"
            data-validation-required-message="Please enter your username."
          />
        </div>
        <div class="form-group my-4">
          <label for="password1">Password </label>
          <input
            class="form-control"
            v-model="credentials.password1"
            type="password"
            id="password1"
            required
            placeholder="Password"
            data-validation-required-message="Please enter your password."
          />
        </div>
        <div class="form-group">
          <label for="password2">Password Confirmation</label>
          <input
            class="form-control"
            v-model="credentials.password2"
            type="password"
            id="password2"
            required
            placeholder="Password2"
            data-validation-required-message="Please enter your password."
          />
        </div>
        <div>
          <button type="submit" class="btn btn-primary mt-4">SignUp</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import AccountErrorList from "@/components/AccountErrorList.vue";

export default {
  name: "SignupView",
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: "",
        password1: "",
        password2: "",
      },
    };
  },
  computed: {
    ...mapGetters(["authError"]),
  },
  methods: {
    ...mapActions(["signup"]),
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
  text-align: center;
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
