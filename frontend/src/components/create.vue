<template>
  <v-container class="d-flex justify-center">
    <v-card class="pa-10" width="600">
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
  </v-container>
</template>


<script>
import Axios from "axios";
import apiUrl from "../url";

export default {
  data: () => ({
    valid: true,
    title: "",
    description: "",
    price: "",
    image: null,

    rules: {
      titleRule: value => !!value || "Title is required",
      descRule: value => !!value || "Description is required",
      priceRule: value => !!value || "Price is required",
      imgRule: value => !!value || "Image is required"
    }
  }),
  methods: {
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
  }
};
</script>