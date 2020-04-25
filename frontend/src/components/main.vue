<template>
  <v-container class="fill-height">
    <v-row>
      <v-col v-for="n in 12" :key="n" md="3">
        <v-card class="mx-auto" max-width="400" link>
          <v-img
            class="white--text align-end"
            height="200px"
            src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
          >
            <v-card-title
              >{{ n }} Complete Python Bootcamp: Go from zero to hero in Python
              3
            </v-card-title>
          </v-img>

          <v-card-subtitle class="pb-0">Number 10</v-card-subtitle>

          <v-card-text class="text--primary">
            <div>
              Learn Python like a Professional! Start from the basics and go all
              the way to creating your own applications and games!
            </div>
          </v-card-text>

          <v-card-actions>
            <v-btn color="orange" text> 19.99${{ tester }} </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
};
</script>
