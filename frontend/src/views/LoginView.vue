<!-- 
frontend\src\views\LoginView.vue
Author: Author : Andre Baldo (http://github.com/andrebaldo/) -->
<template>
<v-container grid-list-xs>
  <v-layout row wrap justify-center align-center>
    <v-flex xs12 md8 lg6>
      <Login />
    </v-flex>
  </v-layout>
</v-container>

</template>

<script>
import Login from "@/modules/authentication/Login.vue";
export default {
  name: "LoginView",
  components: {
    Login
  }
};
</script>
