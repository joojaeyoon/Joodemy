<template>
  <v-container class="pa-0">
    <video controls max-width="100%" width="100%">
      <source v-if="loaded" :src="content.src" type="video/mp4" />Sorry, your browser doesn't support embedded videos.
    </video>
    <v-sheet color="gray" height="100%">
      <v-row class="fill-height mx-5" align="center">
        <div class="display-1 font-weight-bold">{{content.title}}</div>
      </v-row>
    </v-sheet>
  </v-container>
</template>

<script>
import Axios from "axios";
import apiUrl from "../url";

export default {
  data: () => ({
    loaded: false,
    content: {
      id: 1,
      title: "First class",
      time: "03:48",
      src: ""
    }
  }),
  created() {
    const jwt = localStorage.getItem("token");
    Axios.defaults.headers.common["Authorization"] = `jwt ${jwt}`;
    Axios({
      url: `${apiUrl}/api/contents/${this.$route.params.id}`
    }).then(res => {
      this.content = res.data;
      this.content.src = `https://joodemy.s3.ap-northeast-2.amazonaws.com/media/public/${this.content.video}`;
      this.loaded = true;
      console.log(this.content);
    });
  }
};
</script>