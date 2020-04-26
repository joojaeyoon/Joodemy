<template>
  <v-container>
    <v-carousel
      :cycle="false"
      :show-arrows="false"
      max-width="100%"
      height="400"
      hide-delimiters
    >
      <v-carousel-item>
        <v-sheet color="gray" height="100%">
          <v-row class="fill-height" align="center" justify="center">
            <div class="display-1 font-weight-bold">{{ course.title }}</div>
            <div class="subtitle-1 font-weight-medium">
              {{ course.description }}
            </div>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>
    <v-list>
      <v-list-item>
        test
      </v-list-item>
    </v-list>
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
    },
  }),
};
</script>
