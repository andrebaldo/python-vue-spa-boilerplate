<!-- file path: /frontend/src/Views/RegisterVue.vue -->
<template>
  <v-container fill-height align-center justify-center>
    <v-col xs12>
      <Register />
    </v-col>
  </v-container>
</template>

<script>
import Register from "@/components/Register.vue";
export default {
  name: "RegisterView",
  components: {
    Register
  }
};
</script>
