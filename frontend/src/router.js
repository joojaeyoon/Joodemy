import Vue from "vue";
import VueRouter from "vue-router";

import main from "./components/main";
import course from "./components/course";

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
  ],
});
