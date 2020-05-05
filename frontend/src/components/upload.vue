<template>
  <v-container class="d-flex flex-column align-center mt-10">
    <div class="mb-6">
      <v-btn color="primary" @click="upload_select=1">강의 업로드</v-btn>
      <v-btn class="ml-5" color="success" @click="upload_select=2">강의 컨텐츠 업로드</v-btn>
    </div>
    <v-card v-if="upload_select==1" class="pa-10" width="600">
      <v-card-title>강의 생성</v-card-title>
      <v-form ref="createForm" v-model="valid" lazy-validation>
        <v-text-field
          v-model="title"
          name="title"
          :rules="[rules.titleRule]"
          label="Title"
          required
        ></v-text-field>

        <v-textarea
          outlined
          v-model="description"
          :rules="[rules.descRule]"
          name="description"
          label="Description"
        ></v-textarea>
        <v-text-field
          v-model="price"
          name="price"
          :rules="[rules.priceRule]"
          label="Price ($)"
          required
        ></v-text-field>
        <v-file-input
          class="mt-5"
          v-model="image"
          label="Image Input"
          :rules="[rules.imgRule]"
          filled
          prepend-icon="mdi-camera"
        ></v-file-input>
        <v-btn class="primary" @click="clickCreate">Create</v-btn>
      </v-form>
    </v-card>

    <div v-if="upload_select==2">
      <v-select v-model="select" :items="content_title" label="Select Course"></v-select>

      <v-card width="500" class="pa-10 mt-5">
        <v-text-field
          v-model="video_title"
          :rules="content_rules"
          label="title"
          prepend-icon="mdi-format-title"
        ></v-text-field>
        <v-file-input
          class="mt-12"
          :rules="content_rules"
          v-model="video"
          show-size
          label="Upload Video"
          prepend-icon="mdi-video"
        ></v-file-input>
      </v-card>
      <v-btn class="mt-6" color="error" dark large @click="uploadVideo">Upload</v-btn>
    </div>
  </v-container>
</template>

<script>
import Axios from "axios";
import apiUrl from "../url";

export default {
  data: () => ({
    courses: [],
    content_title: [],
    select: null,
    video_title: "",
    video: null,
    content_rules: [value => !!value || "Required."],

    valid: true,
    title: "",
    description: "",
    price: "",
    image: null,

    upload_select: 0,

    rules: {
      titleRule: value => !!value || "Title is required",
      descRule: value => !!value || "Description is required",
      priceRule: value => !!value || "Price is required",
      imgRule: value => !!value || "Image is required"
    }
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
    },
    clickCreate() {
      if (this.$refs.createForm.validate()) {
        const instructor = JSON.parse(localStorage.getItem("user"));

        const formData = new FormData();

        formData.append("instructor", instructor.id);
        formData.append("title", this.title);
        formData.append("description", this.description);
        formData.append("price", this.price);
        formData.append("img", this.image);

        Axios({
          url: `${apiUrl}/api/courses/`,
          method: "POST",
          data: formData,
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
          .then(res => {
            console.log(res);
            if (res.status == 201) {
              alert("강의가 생성되었습니다.");
              window.location.href = "/";
            }
          })
          .catch(err => {
            console.log(err);
          });
      }
    }
  },
  created() {
    const instructor = JSON.parse(localStorage.getItem("user"));
    const jwt = localStorage.getItem("token");
    Axios.defaults.headers.common["Authorization"] = `jwt ${jwt}`;
    Axios({
      url: `${apiUrl}/api/courses/?instructor=${instructor.id}`,
      method: "GET"
    }).then(res => {
      res.data.map((course, idx) => {
        this.content_title.push(idx + 1 + ". " + course.title);
        this.courses.push(course);
      });
    });
  }
};
</script>