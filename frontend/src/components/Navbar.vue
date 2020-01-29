<!-- file path: /frontend/src/components/Navbar.vue -->
<template>
  <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Application</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn 
      rounded color="primary" 
      to="login" 
      v-if="isUserLoggedIn == undefined ||isUserLoggedIn == false" 
      >
        <v-icon left>mdi-login-variant</v-icon>
        
        Login
        </v-btn>
      <v-btn rounded color="primary" to="/" v-if="isUserLoggedIn">Logout</v-btn>
    </v-app-bar>
</template>
<script>
import { mapGetters } from "vuex";
export default {
    Name: 'Navbar',
    computed: {
      ...mapGetters([
        "isUserLoggedIn"
      ])
    }
}
</script>