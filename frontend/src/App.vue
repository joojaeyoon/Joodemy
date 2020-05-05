<template>
  <v-app id="app">
    <!-- <v-navigation-drawer v-model="drawer" app clipped>
      <v-list dense>
        <v-subheader class="mt-4 grey--text text--darken-1">카테고리</v-subheader>
        <v-list>
          <v-list-item v-for="item in categories" :key="item.text" link>
            <v-list-item-avatar>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-avatar>
            <v-list-item-title v-text="item.text" />
          </v-list-item>
        </v-list>
      </v-list>
    </v-navigation-drawer>-->

    <v-app-bar app clipped-left color="indigo" dense>
      <!-- <v-app-bar-nav-icon @click.stop="drawer = !drawer" /> -->
      <v-toolbar-title class="mr-12 align-center">
        <a class="title white--text" style="text-decoration: none !important" href="/">Joodemy</a>
      </v-toolbar-title>
      <v-spacer />

      <v-dialog v-if="!logged" max-width="600">
        <template v-slot:activator="{ on }">
          <v-btn color="primary" dark v-on="on">Login</v-btn>
        </template>
        <login :login="Login" />
      </v-dialog>

      <v-btn v-if="logged" color="primary" dark @click="Logout">Logout</v-btn>

      <v-app-bar-nav-icon v-if="logged" @click="clickUpload">
        <v-icon class="white--text">mdi-upload</v-icon>
      </v-app-bar-nav-icon>
      <v-app-bar-nav-icon v-if="logged" @click="clickProfile">
        <v-icon class="white--text">mdi-account</v-icon>
      </v-app-bar-nav-icon>
    </v-app-bar>

    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import router from "./router";
import login from "./components/login";
import Axios from "axios";

export default {
  name: "App",
  components: { login },
  data: () => ({
    drawer: null,
    logged: false,
    categories: [
      { icon: "mdi-home", text: "Home" },
      { icon: "mdi-dev-to", text: "개발" },
      { icon: "mdi-domain", text: "비즈니스" },
      { icon: "mdi-folder-account", text: "재무 및 회계" },
      { icon: "mdi-laptop", text: "IT 및 소프트웨어" },
      { icon: "mdi-book-open-outline", text: "자기 계발" },
      { icon: "mdi-lead-pencil", text: "디자인" },
      { icon: "mdi-dog-service", text: "라이프스타일" },
      { icon: "mdi-camera", text: "사진" },
      { icon: "mdi-music", text: "음악" }
    ]
  }),
  methods: {
    clickUpload() {
      router.push("/upload");
    },
    clickProfile() {
      router.push("/profile");
    },
    Login() {
      this.logged = true;
    },
    Logout() {
      localStorage.removeItem("token");
      Axios.defaults.headers.common["Authorization"] = "";
      this.logged = false;
    }
  },
  created() {
    if (localStorage.getItem("token") != null) {
      this.Login();
    }
  }
};
</script>
