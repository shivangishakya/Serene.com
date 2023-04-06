<template>
    <div>
      <div class="video-container">
        <video autoplay loop muted>
          <source src="../assets/relax.mp4" type="video/mp4">
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
          <!-- <button @click="goTologin">Login</button> -->
          <router-link to="/login" class="navbar-link">Login</router-link>
          <router-link to="/register" class="navbar-link">Register</router-link>
        </div>
      </div>
      <div class="content">
        <div class="title">
          <h1>WELCOME TO SERENE.COM</h1>
        </div>
        <div class="description">
          <p>At Serene.com, we help to track stress level for all our visitors. 
            Whether you're looking for relaxation techniques, mindfulness tips, 
            or just a moment of peace in your busy day, we've got you covered.</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HomePage',
    metaInfo: {
      title: 'Serene',
      meta: [
        { name: 'description', content: 'This is a description of serene.com.' }
      ]
    }, 
  }
  </script>
  
  <style>
  .video-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    z-index: -1;
  }
  
  .video-container video {
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    background-color: rgba(255, 255, 255, 0.8);
  }
  
  .navbar-left {
    display: flex;
    align-items: center;
  }
  
  .navbar-logo img {
    /* width: 50px;
    height: 50px;
    margin-right: 10px; */
    max-height: 70px;
        max-width: 200px;
        vertical-align: left;
        border: 50;
  }
  
  .navbar-title {
    font-size: 24px;
    font-weight: bold;
  }
  
  .navbar-right {
    display: flex;
  }
  
  .navbar-link {
  padding: 10px 20px;
  background-color: #333;
  color: #fff;
  text-decoration:wavy;
  border-radius: 5px;
}

.navbar-link:hover {
  background-color: #555;
}
  
  .content {
    position: relative;
    z-index: 1;
    text-align: center;
    margin-top: 100px;
  }

  .title {
    font-size: 4rem;
    font-weight: bold;
    text-align: center;
    color: white;
    text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    }

    .description {
    background-color: white;
    padding: 2rem;
    border-radius: 100rem;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    margin-top: 2rem;
    max-width: 80%;
    }

    .details p {
    font-size: 1.5rem;
    line-height: 2rem;
    color: #333;
    }
  
  .content h1 {
    font-size: 48px;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  .content p {
    font-size: 24px;
    line-height: 1.5;
    margin-bottom: 40px;
  }
  </style>
  