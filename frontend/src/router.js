import Vue from "vue";
import VueRouter from "vue-router";

import main from "./components/main";

Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      component: main,
    },
    {
      path: "/course/:id",
    },
  ],
});