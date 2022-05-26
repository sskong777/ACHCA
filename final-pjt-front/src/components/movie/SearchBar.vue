<template>
  <div>
    <v-col
      cols="12"
      class="card d-flex justify-content-center align-items-center"
      style="background-color: black"
    >
      <v-autocomplete
        class="col-10"
        prominent
        v-model="keyword"
        auto-select-first
        :items="movies"
        item-text="title"
        clearable
        solo
        rounded
      >
        <template v-slot:item="{ item }">
          <v-list-item
            style="font-size: 1.2vw"
            link
            :to="{ name: 'movie', params: { moviePk: item.pk } }"
          >
            <v-icon left> mdi-magnify </v-icon>
            {{ item.title }}</v-list-item
          >
        </template>
      </v-autocomplete>
    </v-col>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "SearchBar",
  components: {},
  data: function () {
    return {
      keyword: "",
      result: [],
    };
  },
  computed: {
    ...mapGetters(["movies"]),
  },
  methods: {},
  created() {},
};
</script>

<style>
nav a {
  font-weight: bold;
  color: whitesmoke;
  text-decoration-line: none;
}
</style>
