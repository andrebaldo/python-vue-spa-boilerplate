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
      <v-btn rounded color="primary" to="login">Login</v-btn>
    </v-app-bar>
</template>
<script>
export default {
    Name: 'Navbar'
}
</script>