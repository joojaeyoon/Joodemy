<template>
  <v-container class="d-flex flex-column align-center mt-10">
    <v-select v-model="select" :items="title" label="Select Course"></v-select>

    <v-card width="500" class="pa-10 mt-5">
      <v-text-field
        v-model="video_title"
        :rules="rules"
        label="title"
        prepend-icon="mdi-format-title"
      ></v-text-field>
      <v-file-input
        class="mt-12"
        :rules="rules"
        v-model="video"
        show-size
        label="Upload Video"
        prepend-icon="mdi-video"
      ></v-file-input>
    </v-card>
    <v-btn class="mt-6" color="error" dark large @click="uploadVideo">Upload</v-btn>
  </v-container>
</template>

<script>
import Axios from "axios";
import apiUrl from "../url";

export default {
  data: () => ({
    courses: [],
    title: [],
    select: null,
    video_title: "",
    video: null,
    rules: [value => !!value || "Required."]
  }),
  methods: {
    uploadVideo() {
      const formData = new FormData();
      const course = this.courses[Number(this.select.split(" ")[0][0]) - 1];

      formData.append("title", this.video_title);
      formData.append("video", this.video);
      formData.append("course", course.id);

      Axios({
        url: `${apiUrl}/api/contents/`,
        method: "POST",
        data: formData,
        headers: {
          "Content-Type": "multipart/form-data"
        }
      }).then(res => {
        if (res.status == 201) {
          alert("생성되었습니다.");
          window.location.href = "/";
        }
      });
    }
  },
  created() {
    const instructor = JSON.parse(localStorage.getItem("user"));
    Axios({
      url: `${apiUrl}/api/courses/?instructor=${instructor.id}`,
      method: "GET"
    }).then(res => {
      res.data.map((course, idx) => {
        this.title.push(idx + 1 + ". " + course.title);
        this.courses.push(course);
      });
    });
  }
};
</script>