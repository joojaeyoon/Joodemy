<template>
  <v-container class="pa-0">
    <video controls max-width="100%" width="100%">
      <source src="http://techslides.com/demos/sample-videos/small.mp4" type="video/mp4" />Sorry, your browser doesn't support embedded videos.
    </video>
    <v-sheet color="gray" height="100%">
      <v-row class="fill-height mx-5" align="center">
        <div class="display-1 font-weight-bold">{{content.title}}</div>
      </v-row>
    </v-sheet>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    content: {
      id: 1,
      title: "First class",
      time: "03:48"
    }
  })
};
</script>