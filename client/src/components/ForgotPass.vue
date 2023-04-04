<template>
    <div class="video-container">
        <video autoplay loop muted>
          <source src="../assets/relax2.mp4" type="video/mp4">
        </video>
      </div>
    <div class="forgot-password">
      <h2 class="title">Forgot Password</h2>
      <form class="form" @submit.prevent="submitForm">
        <label for="email" class="label">Email</label>
        <input
          type="email"
          id="email"
          v-model="email"
          class="input"
          placeholder="Enter your email"
          required
        />
        <input
          type="password"
          id="password1"
          class="input"
          placeholder="Enter password"
          required
        />
        <input
          type="password"
          id="password2"
          class="input"
          placeholder="Verify password"
          required
        />
        <button type="submit" class="btn">Submit</button>
      </form>
      <div v-if="showSuccessMessage" class="success-message">
        Password Reset.
      </div>
      <div v-if="showErrorMessage" class="error-message">
        Failed to reset password. Please try again later.
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
        password2: '',
        showSuccessMessage: false,
        showErrorMessage: false
      };
    },
    methods: {
      submitForm() {
        // Call API to send password reset request
        // Replace the following code with your actual API call
        // You can use libraries like axios or fetch to make the API call
        // Example:
        const apiUrl = 'http://127.0.0.1:3000/login/forgot-password/';
        axios.post(apiUrl, { email: this.email,  password: this.password2})
          .then(response => {
            // Show success message
            this.showSuccessMessage = true;
            this.showErrorMessage = false;
          })
          .catch(error => {
            // Show error message
            this.showSuccessMessage = false;
            this.showErrorMessage = true;
          });
  
        // Placeholder code to show success message for demo purposes
        // this.showSuccessMessage = true;
        // this.showErrorMessage = false;
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
  