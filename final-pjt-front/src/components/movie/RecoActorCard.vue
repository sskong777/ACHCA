<template>
  <v-col style="" cols="6" sm="4" md="3" lg="2">
    <v-item v-slot="{ active, toggle }">
      <v-img :src="photoUrl" height="15rem" class="text-right pa-2">
        <v-btn icon dark @click="toggle">
          <v-icon>
            {{ active ? "mdi-heart" : "mdi-heart-outline" }}
          </v-icon>
        </v-btn>
      </v-img>
    </v-item>
    <router-link
      class="text-decoration-none"
      :to="{ name: 'actorProfile', params: { actorPk: actor.pk } }"
    >
      <p id="link">
        {{ actor.actor_name }}
      </p>
    </router-link>
  </v-col>
</template>

<script>
export default {
  name: "RecoActorCard",
  props: {
    actor: Object,
  },
  computed: {
    photoUrl() {
      return `https://image.tmdb.org/t/p/w500/${this.actor.img_key}`;
    },
  },
};
</script>

<style>
#actor-img {
  border-radius: 50%;
}

#link {
  color: aliceblue;
  font-size: 1.2rem;
}
</style>
