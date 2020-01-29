<template>
  <v-snackbar
    v-model="visibility"
    :color="colorCondition ? 'success' : 'error'"
    top
    :timeout="0"
    vertical
  >
    <span>{{message}}</span>
    <v-btn color="primary" @click.native="setSnackbarVisibility(false)">Close</v-btn>
  </v-snackbar>
</template>
<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: 'SnackNotification',
  props: ["colorCondition", "visibility", "message"],

  computed: {
    ...mapGetters(["GetIsSnackbarVisible"])
  },
  methods: {
    ...mapActions(["setSnackbarVisibility"])
  }
};
</script>