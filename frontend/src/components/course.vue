<template>
  <v-container>
    <v-carousel :cycle="false" :show-arrows="false" max-width="100%" height="400" hide-delimiters>
      <v-carousel-item>
        <v-sheet color="gray" height="100%">
          <v-row class="fill-height flex-column" align="center" justify="center">
            <div class="display-3 font-weight-bold">{{ course.title}}</div>
            <div class="headline font-weight-medium">{{ course.description }}</div>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>
    <v-container class="d-flex">
      <v-card width="80%" class="mr-3" elevation="12">
        <v-list two-line>
          <v-container class="pa-0" v-for="c in course.contents" :key="c.id">
            <v-list-item link @click="clickContent(c)">
              <v-list-item-avatar>
                <v-icon>mdi-arrow-right-drop-circle-outline</v-icon>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title v-text="c.title" />
              </v-list-item-content>
              <v-list-item-action>{{c.time}}</v-list-item-action>
            </v-list-item>
            <v-divider></v-divider>
          </v-container>
        </v-list>
      </v-card>
      <v-card class="mx-auto" max-width="400" elevation="12">
        <v-img
          class="white--text align-end"
          height="200px"
          :src="'https://joodemy.s3.ap-northeast-2.amazonaws.com/media/public/'+course.img"
        >
          <v-card-title>{{ course.title }}</v-card-title>
        </v-img>
        <v-card-title>{{ course.price }} $</v-card-title>

        <v-card-actions class="flex-column" width="80%">
          <v-btn v-if="!subscribed" width="100%" height="60" color="red" @click="subscribe">구독</v-btn>
          <v-btn v-if="subscribed" width="100%" height="60" color="red">구독중</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </v-container>
</template>

<script>
import apiUrl from "../url";
import Axios from "axios";

export default {
  props: ["id"],
  data: () => ({
    course: {
      id: 1,
      img: "1-wjwwex.png",
      title: "",
      description: "",
      instructor: "",
      price: "",

      contents: []
    },
    subscribed: false,
    user: {}
  }),
  created() {
    const id = this.$route.params.id;

    const user = JSON.parse(localStorage.getItem("user"));

    this.user = user;

    Axios({
      url: `${apiUrl}/api/courses/${id}/`,
      method: "GET"
    }).then(res => {
      if (res.status == 200) {
        this.course = res.data;
      }
    });

    Axios({
      url: `${apiUrl}/api/subscribes/`,
      method: "GET",
      params: {
        student: user.id
      }
    }).then(res => {
      res.data.courses.map(c => {
        if (c == id) {
          this.subscribed = true;
        }
      });
    });
  },
  methods: {
    subscribe() {
      const jwt = localStorage.getItem("token");
      Axios.defaults.headers.common["Authorization"] = `jwt ${jwt}`;
      Axios({
        url: `${apiUrl}/api/subscribes/`,
        method: "POST",
        data: {
          student: this.user.id,
          course: this.course.id
        }
      }).then(res => {
        console.log(res);
        this.subscribed = true;
      });
    },
    clickContent(content) {
      if (this.subscribed) {
        window.location.href = `/contents/${content.id}`;
      } else {
        // TODO error handling
      }
    }
  }
};
</script>
