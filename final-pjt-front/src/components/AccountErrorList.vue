<template>
  <div class="account-error-list">
    <p v-for="(errors, field) in authError" :key="field">
      <!-- {{ field }} -->
      <ul>
        <div v-for="(error, idx) in errors" :key="idx">
          <!-- {{ error }} -->
          등록되지 않은 아이디이거나 아이디 또는 비밀번호를 잘못 입력했습니다.
        </div>
      </ul>
    </p>

  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  
  export default {
    name: 'AccountErrorList',
    computed: {
      ...mapGetters(['authError'])
    },
  }
</script>

<style>
  .account-error-list {
    color: red;
  }
</style>
