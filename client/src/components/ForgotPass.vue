<template>
  <div>
    <div class="video-container">
      <video autoplay muted loop>
        <source src="../assets/relax-3.mp4" type="video/mp4">
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
          <button class="navbar-link" @click="homepage">Back</button>
        </div>
    </div>
    <div class="video-container">
        <video autoplay loop muted>
          <source src="../assets/relax2.mp4" type="video/mp4">
        </video>
      </div>
    <div class="forgot-password">
      <h2 class="title">Forgot Password</h2>
      <form class="form" @submit.prevent="submitForm">
        <!-- <label for="email" class="label">Email</label> -->
        <input
          type="email"
          id="email"
          v-model="email"
          class="input"
          placeholder="Enter your email"
          required
        />
        <button type="submit" class="btn">Submit</button>
      </form>
      <!-- <div v-if="showSuccessMessage" class="success-message">
        Password Reset.
      </div>
      <div v-if="showErrorMessage" class="error-message">
        Failed to reset password. Please try again later.
      </div> -->
    </div>
  </div>
  </template>
  
  <script>
  import axios from 'axios';
  /* eslint-disable */
  export default {
    data() {
      return {
        email: '',
      };
    },
    methods: {
      homepage() {
        window.location.href = '/';
      },
      submitForm() {
        const apiUrl = 'http://127.0.0.1:3000/login/forgot-password/';
        axios.post(apiUrl, { email: this.email})
          .then(response => {
            alert("Password Sent")
          })
          .catch(error => {
            // Show error message
            alert("No Email Id")
          });
      }
    }
  };
  </script>
  
  <style scoped>
  .forgot-password {
    max-width: 400px;
    margin: 0 auto;
  }
  
  .title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  .form {
    margin-bottom: 20px;
  }
  
  .label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
  }
  
  .input {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
  }
  
  .btn {
    background-color: #007bff;
    color: #fff;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
  }
  
  .success-message,
  .error-message {
    margin-top: 10px;
    padding: 10px;
    text-align: center;
  }
  
  .success-message {
    background-color: #28a745;
    color: #fff;
  }
  
  .error-message {
    background-color: #dc3545;
    color: #fff;
  }
  </style>
  