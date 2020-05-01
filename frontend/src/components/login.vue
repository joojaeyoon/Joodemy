<template>
  <v-container class="d-flex justify-center">
    <v-card v-if="isLogin" class="pa-12 ma-0" width="100%" height="100%">
      <v-form ref="loginForm" v-model="valid" lazy-validation>
        <v-card-title>Login</v-card-title>
        <v-text-field
          :counter="10"
          v-model="username"
          :rules="rules.nameRules"
          label="Username"
          required
        ></v-text-field>

        <v-text-field
          v-model="password"
          :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required, rules.min]"
          :type="show ? 'text' : 'password'"
          name="password"
          label="Password"
          hint="At least 8 characters"
          @click:append="show = !show"
        ></v-text-field>

        <v-btn :disabled="!valid" color="primary" class="mr-4" @click="loginValidate">Login</v-btn>
        <v-btn color="error" class="mr-4" @click="swap">Register</v-btn>
      </v-form>
    </v-card>

    <v-card v-if="!isLogin" class="pa-12 ma-0" width="100%" height="100%">
      <v-card-title>Register</v-card-title>
      <v-form ref="registerForm" v-model="valid" lazy-validation>
        <v-text-field
          :counter="10"
          v-model="username"
          :rules="rules.nameRules"
          label="Username"
          required
        ></v-text-field>
        <v-text-field label="email" v-model="email" :rules="rules.emailRules" required></v-text-field>

        <v-text-field
          v-model="password1"
          :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required, rules.min]"
          :type="show ? 'text' : 'password'"
          name="password1"
          label="Password"
          hint="At least 8 characters"
          counter
          @click:append="show = !show"
        ></v-text-field>
        <v-text-field
          v-model="password2"
          :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required, rules.min, (password1===password2)]"
          :type="show ? 'text' : 'password'"
          name="password2"
          label="Password"
          hint="At least 8 characters"
          counter
          @click:append="show = !show"
        ></v-text-field>

        <v-btn :disabled="!valid" color="primary" class="mr-4" @click="registerValidate">Register</v-btn>
        <v-btn color="error" class="mr-4" @click="swap">Login</v-btn>
      </v-form>
    </v-card>
  </v-container>
</template>


<script>
import axios from "axios";
import apiUrl from "../url";

export default {
  props: ["login"],
  data: () => ({
    isLogin: true,
    valid: true,
    username: "",
    password: "",
    email: "",
    password1: "",
    password2: "",

    show: false,
    rules: {
      required: value => !!value || "Required.",
      min: v => v.length >= 8 || "Min 8 characters",
      checkPassword: () =>
        this.password1 === this.password2 || "Two Password are different!",
      nameRules: [
        v => !!v || "Name is required",
        v => (v && v.length <= 10) || "Name must be less than 10 characters"
      ],
      emailRules: [
        v => !!v || "E-mail is required",
        v => /.+@.+\..+/.test(v) || "E-mail must be valid"
      ]
    }
  }),

  methods: {
    loginValidate() {
      const vaild = this.$refs.loginForm.validate();
      if (vaild) {
        axios(`${apiUrl}/api/auth/login/`, {
          method: "POST",
          data: {
            username: this.username,
            password: this.password
          }
        }).then(res => {
          localStorage.setItem("token", res.data.token);
          localStorage.setItem("user", JSON.stringify(res.data.user));
          axios.defaults.headers.common[
            "Authorization"
          ] = `jwt ${res.data.token}`;
          this.login();
        });
      }
    },
    registerValidate() {
      const vaild = this.$refs.registerForm.validate();
      if (vaild) {
        axios(`${apiUrl}/api/auth/registration/`, {
          method: "POST",
          data: {
            username: this.username,
            email: this.email,
            password: this.password1
          }
        }).then(res => {
          localStorage.setItem("token", res.data.token);
          localStorage.setItem("user", JSON.stringify(res.data.user));
          axios.defaults.headers.common[
            "Authorization"
          ] = `jwt ${res.data.token}`;
          this.login();
        });
      }
    },
    swap() {
      this.isLogin = !this.isLogin;
    }
  }
};
</script>