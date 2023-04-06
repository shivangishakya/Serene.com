<template>
    <div>
        <div class="video-container">
        <video autoplay loop muted>
          <source src="../assets/relax2.mp4" type="video/mp4">
        </video>
      </div>
        <div class="navbar">
        <div class="navbar-left">
          <div class="navbar-logo">
            <img src="../assets/serenelogo.png" alt="Logo">
          </div>
          <div class="navbar-title">Serene.Com</div>
        </div>
        <div class="navbar-right">
          <router-link to="/" class="navbar-link">Log Out</router-link>
        </div>
    </div>
    <div class="background">
      <div class="container">
        <!-- <h1>Our Services</h1> -->
        <ul class="services">
          <li @click="redirectTo('http://localhost:8080/survey')">Calculate Your Stress</li>
          <li @click="redirectTo('https://example.com/service2')">Manage Profile</li>
          <li @click="redirectTo('https://example.com/service3')">Add Recipient</li>
          <li @click="redirectTo('https://www.helpguide.org/')">Mental Health Guide</li>
        </ul>
      </div>
    </div>
</div>
  </template>
  
  <script>
  export default {
    methods: {
      redirectTo(url) {
        window.location.href = url;
      },
    },
  };
  </script>
  
  <style scoped>
  .background {
    /* background-image: url('/path/to/background.jpg'); */
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .container {
    max-width: 800px;
    padding: 0 20px;
    text-align: center;
  }
  
  h1 {
    color: rgb(235, 192, 192);
    font-size: 48px;
    margin-bottom: 50px;
  }
  
  .services {
    list-style-type: none;
    padding: 0;
    margin: 0;
  }
  
  .services li {
    color: whitesmoke;
    background-color: rgba(202, 21, 21, 0.567);
    padding: 30px;
    margin-bottom: 20px;
    border-radius: 50px;
    font-size: 24px;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .services li:hover {
    background-color: rgba(161, 126, 30, 0.51);
    transform: scale(1.05);
  }
  </style>
  