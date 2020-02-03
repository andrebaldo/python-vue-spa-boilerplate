<!-- 
frontend\src\components\Navbar.vue 
Author: Author : Andre Baldo (http://github.com/andrebaldo/) -->
<template>
  <v-app-bar app color="indigo" dark>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
    <v-toolbar-title>Application</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn
      rounded
      color="primary"
      to="login"
      v-if="getIsUserLoggedIn == undefined ||getIsUserLoggedIn == false"
    >
      <v-icon left>mdi-login-variant</v-icon>Login
    </v-btn>
    <v-btn rounded color="grey darken-2" to="/" v-if="getIsUserLoggedIn" @click="processLogout()">
     Logout <v-icon right>mdi-logout-variant</v-icon>
    </v-btn>
  </v-app-bar>
</template>
<script>
import { mapGetters, mapActions } from "vuex";
export default {
  Name: "Navbar",
  computed: {
    ...mapGetters(["getIsUserLoggedIn"])
  },
  methods: {
    ...mapActions(["logout"]),
    processLogout(){
      this.logout({controllerReference:this})
      .then(function(ctrl){
        ctrl.$router.push('login')
      })
    }
  }
};
</script>