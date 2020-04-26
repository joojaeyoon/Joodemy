<template>
  <v-container class="fill-height">
    <v-row>
      <v-col v-for="course in courses" :key="course.id" md="3">
        <v-card
          class="mx-auto"
          max-width="400"
          link
          v-on:click="clickCourse(course.id)"
        >
          <v-img class="white--text align-end" height="200px" :src="course.img">
            <v-card-title>{{ course.title }} </v-card-title>
          </v-img>

          <v-card-subtitle class="pb-0">{{
            course.instructor
          }}</v-card-subtitle>

          <v-card-text class="text--primary">
            <div>
              {{ course.description }}
            </div>
          </v-card-text>

          <v-card-actions>
            <v-btn color="orange" text> {{ course.price }}</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import router from "../router";

export default {
  name: "Main",

  data: () => ({
    courses: [
      {
        id: 1,
        img: "https://cdn.vuetifyjs.com/images/cards/docks.jpg",
        title: "Complete Python Bootcamp: Go from zero to hero in Python3",
        description:
          "Learn Python like a Professional! Start from the basics and go all the way to creating your own applications and games!",
        instructor: "Joo",
        price: "19.99$",
      },
      {
        id: 2,
        img: "https://cdn.vuetifyjs.com/images/cards/docks.jpg",
        title: "Complete Python Bootcamp: Go from zero to hero in Python3",
        description:
          "Learn Python like a Professional! Start from the basics and go all the way to creating your own applications and games!",
        instructor: "Joo",
        price: "19.99$",
      },
    ],
  }),

  methods: {
    clickCourse: function(courseId) {
      router.push(`/courses/${courseId}`);
    },
  },
};
</script>
