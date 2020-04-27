<template>
  <v-container class="d-flex flex-column align-center mt-10">
    <v-select :items="courses" label="Select Course"></v-select>

    <v-card v-for="card in cards" :key="card" width="400" class="pa-10 mt-5">
      <v-text-field :rules="rules" label="title" prepend-icon="mdi-format-title"></v-text-field>
      <v-file-input show-size label="Upload Video" prepend-icon="mdi-video"></v-file-input>
    </v-card>

    <div class="mt-6">
      <v-btn color="primary" large @click="clickPlus">
        <v-icon>mdi-plus</v-icon>
      </v-btn>
      <v-btn class="ml-5" color="error" large @click="clickMinus">
        <v-icon>mdi-minus</v-icon>
      </v-btn>
    </div>
    <v-btn class="mt-6" color="error" dark large>Upload</v-btn>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    cards: 1,
    courses: ["course1", "course2", "course3"],
    rules: [
      value => !!value || "Required.",
      value => (value || "").length <= 20 || "Max 20 characters"
    ]
  }),
  methods: {
    clickPlus() {
      this.cards += 1;
    },
    clickMinus() {
      if (this.cards != 1) this.cards -= 1;
    }
  }
};
</script>