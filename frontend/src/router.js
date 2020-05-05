import Vue from "vue";
import VueRouter from "vue-router";

import main from "./components/main";
import course from "./components/course";
import video from "./components/video";
import upload from "./components/upload";
import login from "./components/login";
import create from "./components/create";

Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      component: main,
    },
    {
      path: "/courses/:id",
      component: course,
    },
    {
      path: "/contents/:id",
      component: video,
    },
    {
      path: "/upload",
      component: upload,
    },
    {
      path: "/login",
      component: login,
    },
    {
      path: "/create",
      component: create,
    },
  ],
});
