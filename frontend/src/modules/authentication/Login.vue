<!-- file path: /frontend/src/components/Login.vue -->
<template>
  <v-card>
    <v-card-title primary-title>
      <h1>Login</h1>
    </v-card-title>
    <v-card-text>
      <v-form rounded v-model="isLoginFormValid">
        <v-text-field
          name="email"
          label="Email*"
          id="email"
          v-model="email"
          prepend-icon="mdi-account-circle"
          required
          :rules="[checkIsRequired(email), validateEmail(email)]"
          type="email"
        ></v-text-field>

        <v-text-field
          name="password"
          label="Password*"
          id="password"
          v-model="password"
          :type="getPasswordFieldType()"
          prepend-icon="mdi-lock"
          :append-icon="getShowPasswordApendIcon()"
          @click:append="toggleShowPassword()"
          required
        ></v-text-field>

        <div class="text-center">
          <v-progress-circular indeterminate color="primary" v-if="isProcessing"></v-progress-circular>
        </div>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <router-link to="register">Go to Register</router-link>
      <v-spacer></v-spacer>
      <v-btn
        color="success"
        :disabled="!isLoginFormValid || isProcessing || GetIsSnackbarVisible"
        @click="login({email:email, password:password})"
      >Login</v-btn>
    </v-card-actions>
    <SnackNotification
      v-bind:visibility="GetIsSnackbarVisible"
      v-bind:colorCondition="getIsUserLoggedIn"
      v-bind:message="getLoginProcessMessage"
    />
  </v-card>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import SnackNotification from "@/modules/notification/SnackNotification.vue";
export default {
  name: "Login",
  data: function() {
    return {
      showPassword: false,
      isLoginFormValid: false,
      email: "",
      password: "",
      mobilePhone: ""
    };
  },
  methods: {
    getPasswordFieldType: function() {
      if (this.showPassword) {
        return "text";
      } else {
        return "password";
      }
    },
    toggleShowPassword: function() {
      this.showPassword = !this.showPassword;
    },
    getShowPasswordApendIcon: function() {
      if (this.showPassword) {
        return "mdi-eye";
      } else {
        return "mdi-eye-off";
      }
    },
    checkIsRequired: function(value, errorMessage) {
      if (!errorMessage) {
        errorMessage = "This field is required";
      }
      return !!value || errorMessage;
    },
    ...mapActions(["authenticateUserAndSetToken"]),
    validateEmail(email) {
      var re = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
      return (
        re.test(String(email).toLowerCase()) ||
        "Oops, this doesn't looks like rigth, can you check please?"
      );
    },
    login(loginData){
      loginData.controllerReference = this;
      this.authenticateUserAndSetToken(loginData)
      .then(function(controller){
        controller.$router.push('/')
      })
    }
  },
  computed: {
    ...mapGetters([
      "getLoginProcessMessage",
      "isProcessing",
      "getIsUserLoggedIn",
      "GetIsSnackbarVisible"
    ])
  },
  components: {
    SnackNotification
  }
};
</script>