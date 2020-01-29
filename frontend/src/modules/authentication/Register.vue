<!-- file path: /frontend/src/components/Register.vue -->
<template>
  <v-card>
    <v-card-title primary-title>
      <h1>Register</h1>
    </v-card-title>
    <v-card-text>
      <v-form rounded v-model="isRegisterFormValid">
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
          counter="50"
          required
          :rules="[checkIsRequired(password), checkMinLenght(password.length,8)]"
          loading
        >
          <template v-slot:progress>
            <v-progress-linear :value="progress(8)" :color="color(8)" absolute height="7"></v-progress-linear>
          </template>
        </v-text-field>

        <v-text-field
          name="mobilePhone"
          label="Mobile Phone"
          id="mobilePhone"
          v-model="mobilePhone"
          prepend-icon="mdi-phone"
          type="tel"
        ></v-text-field>

        <div class="text-center">
          <v-progress-circular indeterminate color="primary" v-if="isProcessing"></v-progress-circular>
        </div>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <router-link to="login">Go to login</router-link>
      <v-spacer></v-spacer>
      <v-btn
        color="success"
        :disabled="!isRegisterFormValid || isProcessing || GetIsSnackbarVisible"
        @click="registerNewUser({email:email, password:password, mobilePhone:mobilePhone})"
      >
        <v-icon left>mdi-account-plus</v-icon>Register
      </v-btn>
      <SnackNotification
        v-bind:visibility="GetIsSnackbarVisible"
        v-bind:colorCondition="getIsRegistrationProcessSucceed"
        v-bind:message="getRegistrationProcessMessage"
      />
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import SnackNotification from "@/modules/notification/SnackNotification.vue";

export default {
  name: "Register",
  data: function() {
    return {
      showPassword: false,
      isRegisterFormValid: false,
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
    checkMinLenght(valueLenght, minLength, errorMessage) {
      if (!errorMessage) {
        errorMessage = `Min length is ${minLength}`;
      }
      return (!!valueLenght && valueLenght >= minLength) || errorMessage;
    },
    progress(minLength) {
      return Math.min(100, (this.password.length / minLength) * 100);
    },
    color(minLength) {
      let selectedColorIndex = 0;
      if (this.progress(minLength) < 40) {
        selectedColorIndex = 0;
      } else if (
        this.progress(minLength) > 40 &&
        this.progress(minLength) < 100
      ) {
        selectedColorIndex = 1;
      } else {
        selectedColorIndex = 2;
      }
      return ["error", "warning", "success"][selectedColorIndex];
    },
    ...mapActions(["registerNewUser", "setSnackbarVisibility"]),
    validateEmail(email) {
      var re = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
      return (
        re.test(String(email).toLowerCase()) ||
        "Oops, this doesn't looks like rigth, can you check please?"
      );
    }
  },
  computed: {
    ...mapGetters([
      "getIsRegistrationProcessSucceed",
      "getRegistrationProcessMessage",
      "isProcessing",
      "GetIsSnackbarVisible"
    ])
  },
  components: {
    SnackNotification
  }
};
</script>