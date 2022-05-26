<template>
  <div class="review-list">
    <div v-if="isLoggedIn">
      <review-list-form></review-list-form>
    </div>
    <ul id="ul-tag">
      <review-list-item
        v-for="review in reviews"
        :review="review"
        :key="review.pk"
      >
      </review-list-item>
    </ul>
  </div>
</template>

<script>
import ReviewListItem from "@/components/movie/ReviewListItem.vue";
import ReviewListForm from "@/components/movie/ReviewListForm.vue";
import { mapGetters } from "vuex";

export default {
  name: "ReviewList",
  components: { ReviewListForm, ReviewListItem },
  props: { reviews: Array },
  computed: {
    ...mapGetters(["isLoggedIn"]),
  },
};
</script>

<style>
#ul-tag {
  list-style: none;
}
</style>
