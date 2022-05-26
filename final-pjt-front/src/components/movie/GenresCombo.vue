<template>
  <v-container class="pe-2 row" fluid>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="action"
      label="액션"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="mohum"
      label="모험"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="ani"
      label="애니메이션"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="comedy"
      label="코미디"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="crime"
      label="범죄"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="docu"
      label="다큐멘터리"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="drama"
      label="드라마"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="family"
      label="가족"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="fantazy"
      label="판타지"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="history"
      label="역사"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="scary"
      label="공포"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="music"
      label="음악"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="mistery"
      label="미스터리"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="ramance"
      label="로맨스"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="SF"
      label="SF"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="TV"
      label="TV 영화"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="thriler"
      label="스릴러"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="war"
      label="전쟁"
    ></v-checkbox>
    <v-checkbox
      dark
      @click="genres_check"
      class="col-4 col-md-3"
      v-model="west"
      label="서부"
    ></v-checkbox>
  </v-container>
</template>

<script>
export default {
  name: "GenresCombo",
  data() {
    return {
      action: false,
      mohum: false,
      ani: false,
      comedy: false,
      crime: false,
      docu: false,
      drama: false,
      family: false,
      fantazy: false,
      history: false,
      scary: false,
      music: false,
      mistery: false,
      ramance: false,
      SF: false,
      TV: false,
      thriler: false,
      war: false,
      west: false,
      select: [],
    };
  },
  methods: {
    genres_check() {
      this.select = [];
      if (this.action) {
        this.select.push(28);
      }
      if (this.mohum) {
        this.select.push(12);
      }
      if (this.ani) {
        this.select.push(16);
      }
      if (this.comedy) {
        this.select.push(35);
      }
      if (this.crime) {
        this.select.push(80);
      }
      if (this.docu) {
        this.select.push(99);
      }
      if (this.drama) {
        this.select.push(18);
      }
      if (this.family) {
        this.select.push(10751);
      }
      if (this.fantazy) {
        this.select.push(14);
      }
      if (this.history) {
        this.select.push(36);
      }
      if (this.scary) {
        this.select.push(27);
      }
      if (this.music) {
        this.select.push(10402);
      }
      if (this.mistery) {
        this.select.push(9648);
      }
      if (this.ramance) {
        this.select.push(10749);
      }
      if (this.SF) {
        this.select.push(878);
      }
      if (this.TV) {
        this.select.push(10770);
      }
      if (this.thriler) {
        this.select.push(53);
      }
      if (this.war) {
        this.select.push(10752);
      }
      if (this.west) {
        this.select.push(37);
      }
      this.$emit("search-genres", this.select);
    },
  },
};
</script>

<style></style>
