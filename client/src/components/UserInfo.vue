<template>
<div>
    <div class="video-container">
      <video autoplay muted loop>
        <source src="../assets/relax-4.mp4" type="video/mp4">
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
          <button class="navbar-link" @click="welcomepage">Back</button>
          <button class="navbar-link" @click="handleLogout">Log Out</button>
          <!-- <router-link to="/" class="navbar-link">Log Out</router-link> -->
        </div>
    </div>
    <div class="page-title" :style="{ backgroundColor: '#f2f2f2' }">
      <h2>User Information</h2>
    </div>
    <div class="user-form">
      <!-- <h2>{{ user.name }}</h2> -->
      <form @submit.prevent="saveUserData">
        <div class="form-group">
          <label for="name" style="color: cornsilk;">Name</label>
          <input type="name" id="name" v-model="user.name" class="form-control" required>
        </div>
        <div class="form-group">
          <label for="email" style="color: cornsilk;">Phone Number</label>
          <input type="phone" v-model="user.phone" class="form-control" >
        </div>
        <div class="form-group">
          <label for="address" style="color: cornsilk;">Address</label>
          <textarea id="address" v-model="user.address" class="form-control" ></textarea>
        </div>
        <!-- add more form inputs for additional user information as needed -->
        <button type="submit" class="btn btn-primary">Save</button>
      </form>
    </div>
</div>
</template>
  
  <script>
  import { reactive, onMounted } from 'vue';
  import axios from 'axios';
  
  export default {
    setup() {
      const user = reactive({
        name: '',
        phone: '',
        address: '',
        // add more user information as needed
      });
      const username = localStorage.getItem('username');
      const password = localStorage.getItem('password');

      const apiUrl1 = 'http://127.0.0.1:3000/get-user-info';
      const apiUrl2 = 'http://127.0.0.1:3000/put-user-info';
      const encodedCredentials = btoa(`${username}:${password}`);
      const headers = { 'Authorization': `Basic ${encodedCredentials}` };
      const getUserData = async () => {
        try {
          const response = await axios.get(apiUrl1, {headers});
          user.name = response.data.name === "None" ? "" : response.data.name;
          user.phone = response.data.phone === "None" ? "" : response.data.phone;
          user.address = response.data.address === "None" ? "" : response.data.address;
          console.log(user.name)
          // add more user information as needed
        } catch (error) {
          console.error(error);
        }
      };
  
      const saveUserData = async () => {
        try {
          const response = await axios.post(apiUrl2, user, {headers});
          console.log(response.data); // handle success response as needed
          alert("User Data is saved")
        } catch (error) {
          console.error(error);
        }
      };
  
      onMounted(() => {
        getUserData();
      });
  
      return { user, saveUserData };
    },
    methods: {
    handleLogout() {
      localStorage.clear();
      window.location.href = '/';
    },
    welcomepage() {
        window.location.href = '/welcome';
    }
    }
  };
  </script>
  
  <style scoped>
  .navbar-link {
  padding: 10px 20px;
  background-color: #333;
  color: #fff;
  text-decoration:wavy;
  border-radius: 5px;
}

  .user-form {
    max-width: 500px;
    margin: 0 auto;
    background-color: rgba(58, 125, 183, 0.707);
    padding: 50px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  .form-group {
    margin-bottom: 20px;
    width: 95%;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }
  
  input,
  textarea {
    display: block;
    width: 100%;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
    box-shadow: none;
    font-size: 16px;
    line-height: 1.5;
  }
  
  button[type="submit"] {
    display: block;
    margin-top: 20px;
    padding: 10px 20px;
    border-radius: 5px;
    background-color: #007bff;
    color: #fff;
    border: none;
    box-shadow: none;
    font-size: 16px;
    line-height: 1.5;
    cursor: pointer;
  }
  
  button[type="submit"]:hover {
    background-color: #0069d9;
  }
  </style>
  