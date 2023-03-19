<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png" /> -->
  <Homepage msg="Welcome to Serene.Com" />
</template>

<script>
import Homepage from "./components/Homepage.vue";

export default {
  name: "App",
  components: {
    Homepage,
},
};
</script>

<style>
html, body {
  height: 100%;
  margin: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0;
  font-style:italic;
  font-weight:900;
  height:100%;
  /* background-image: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)),url(./assets/Relaxing_Full_HD_Film_Ocean_Live_Wallpaper_Dreamscene.gif);
  background-size: 100% auto; */
}
</style>
