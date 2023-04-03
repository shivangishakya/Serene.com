
<template>
    <div>
      <div class="video-container">
        <video autoplay loop muted>
          <source src="../assets/relax1.mp4" type="video/mp4">
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
        </div>
      </div>
      <div class="login-container">
       <div class="login-box">
         <h2 class="login-title">Login</h2>
         <form>
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" v-model="username">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" v-model="password">
            </div>
            <button type="submit" @click.prevent="submitForm">Submit</button>
         </form>
         <div class="links">
            <router-link to="/forgot-password" class="forgot-password-link">Forgot Password?</router-link>
            <span class="separator">|</span>
            <router-link to="/register" class="register-link">Register</router-link>
         </div>
       </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
      }
    },
    methods: {
      submitForm() {
        // do something with the username and password
        console.log('Username:', this.username)
        console.log('Password:', this.password)
        this.$router.push({ name: "SurveyR" });
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
  
  .login-container {
    display:grid;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 70vh;
    overflow: hidden;
    cursor: pointer;
  }

  .login-box {
    background-color: rgba(255, 255, 255, 0.8);
    padding: 20px;
    border-radius: 5px;
    text-align: center;
  }
  
  .login-title {
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
  
  