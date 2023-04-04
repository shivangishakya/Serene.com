
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
          <router-link to="/" class="navbar-link">Home</router-link>
          <router-link to="/login" class="navbar-link">Login</router-link>
        </div>
      </div>
      <div class="register-container">
       <div class="register-box">
         <h2 class="register-title">New User Registration</h2>
         <form>
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" v-model="username">
            </div>
            <div class="form-group">
                <label for="password1">Password</label>
                <input type="password" id="password1" name="password1" v-model="password">
            </div>
            <div class="form-group">
                <label for="password2">Verify Password</label>
                <input type="password" id="password2" name="password2" v-model="password">
            </div>
            <button type="submit" @click.prevent="submitForm">Submit</button>
         </form>
       </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        username: '',
        password1: '',
        password2: '',
      }
    },
    methods: {
      submitForm() {
        // do something with the username and password
        console.log('Username:', this.username)
        console.log('Password:', this.password2)
        const apiUrl = 'http://127.0.0.1:3000/register/';

        axios.post(apiUrl, { "username":this.username, "password": this.password})
          .then(response => {
            // Handle the API response
            console.log(response.data);
            this.$router.push({ name: "LoginModal" });
          })
          .catch(error => {
            // Handle the API error
            console.error(error);
            this.$router.push({ name: "Homepage" });
          });
      }
    }
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
    margin-left: 10px;
    font-size: 18px;
    cursor: pointer;
  }
  
  .register-container {
    display:grid;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 70vh;
    overflow: hidden;
    cursor: pointer;
  }

  .register-box {
    background-color: rgba(255, 255, 255, 0.8);
    padding: 20px;
    border-radius: 5px;
    text-align: center;
  }
  
  .register-title {
    font-size: 2rem;
    margin-bottom: 20px;
  }

  .form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
    text-align: left;
  }
  
  label {
    font-weight: bold;
    margin-bottom: 5px;
  }
  
  input[type="text"], input[type="password"] {
    padding: 10px;
    border-radius: 5px;
    border: none;
  } 
  
  button[type="submit"] {
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .links {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
  }
  
  .forgot-password-link, .register-link {
    margin-left: 10px;
    margin-right: 10px;
    cursor: pointer;
  }
  
  .separator {
    font-weight: bold;
    margin-left: 10px;
    margin-right: 10px;
  }
  
  .router-link-active {
    font-weight: bold;
  }
  </style>
  
  