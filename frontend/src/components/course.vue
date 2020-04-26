<template>
  <v-container>
    <v-carousel :cycle="false" :show-arrows="false" max-width="100%" height="400" hide-delimiters>
      <v-carousel-item>
        <v-sheet color="gray" height="100%">
          <v-row class="fill-height" align="center" justify="center">
            <div class="display-1 font-weight-bold">{{ course.title }}</div>
            <div class="subtitle-1 font-weight-medium">{{ course.description }}</div>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>
    <v-container class="d-flex">
      <v-card width="80%" class="mr-3" elevation="12">
        <v-list two-line>
          <v-container class="pa-0" v-for="c in course.classes" :key="c.id">
            <v-list-item link>
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
        <v-img class="white--text align-end" height="200px" :src="course.img">
          <v-card-title>{{ course.title }}</v-card-title>
        </v-img>
        <v-card-title>{{ course.price }}</v-card-title>

        <v-card-actions class="flex-column" width="80%">
          <v-btn width="100%" height="60" color="red">장바구니</v-btn>
          <v-btn width="100%" height="60" class="ma-0 mt-3">구매하기</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    course: {
      id: 1,
      img: "https://cdn.vuetifyjs.com/images/cards/docks.jpg",
      title: "Complete Python Bootcamp: Go from zero to hero in Python3",
      description:
        "Learn Python like a Professional! Start from the basics and go all the way to creating your own applications and games!",
      instructor: "Joo",
      price: "19.99$",

      classes: [
        { id: 1, title: "First class", time: "03:48" },
        { id: 2, title: "Second class", time: "05:22" },
        { id: 3, title: "Third class", time: "04:54" }
      ]
    }
  })
};
</script>
