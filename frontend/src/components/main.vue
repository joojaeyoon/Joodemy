<template>
  <v-container class="fill-height">
    <v-row>
      <v-col v-for="course in courses" :key="course.id" md="3">
        <v-card class="mx-auto" max-width="400" link v-on:click="clickCourse(course.id)">
          <v-img
            class="white--text align-end"
            height="200px"
            :src="'https://joodemy.s3.ap-northeast-2.amazonaws.com/media/public/'+course.img"
          >
            <v-card-title class="body-2">{{ course.title }}</v-card-title>
          </v-img>

          <v-card-subtitle class="pb-0">
            {{
            course.instructor
            }}
          </v-card-subtitle>

          <v-card-text class="text--primary">
            <div>{{ course.description }}</div>
          </v-card-text>

          <v-card-actions>
            <v-btn color="orange" text>{{ course.price }} $</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import router from "../router";
import Axios from "axios";
import apiUrl from "../url";

export default {
  name: "Main",

  data: () => ({
    courses: []
  }),

  methods: {
    clickCourse: function(courseId) {
      router.push(`/courses/${courseId}`);
    }
  },
  created() {
    Axios({
      url: `${apiUrl}/api/courses/`,
      method: "GET"
    }).then(res => {
      this.courses = res.data;
    });
  }
};
</script>
