<!-- 
frontend\src\views\RegisterView.vue
Author: Author : Andre Baldo (http://github.com/andrebaldo/) -->
<template>
<v-container grid-list-xs>
  <v-layout row wrap justify-center align-center>
    <v-flex xs12 md8 lg6>
      <Register />
    </v-flex>
  </v-layout>
</v-container>

</template>

<script>
import Register from "@/modules/authentication/Register.vue";
export default {
  name: "RegisterView",
  components: {
    Register
  }
};
</script>
