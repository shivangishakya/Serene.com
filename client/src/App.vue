<template>
  <router-view></router-view>
  <!-- <Homepage/> -->
</template>

<script>
/* eslint-disable */
import Homepage from './components/Homepage.vue';

export default {
  name: 'App',
  components: {
    Homepage,
}
}
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
}
</style>
