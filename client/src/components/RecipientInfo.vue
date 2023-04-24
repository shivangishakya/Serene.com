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
          <button class="navbar-link" @click="callApi">Send Report</button>
          <button class="navbar-link" @click="welcomepage">Back</button>
          <button class="navbar-link" @click="handleLogout">Log Out</button>
        </div>
    </div>
    <div class="page-title" :style="{ backgroundColor: '#f2f2f2' }">
      <h2>Add Recipient Emails</h2>
    </div>
    <div class="email-container">
    <form @submit.prevent="addEmail">
      <div v-for="i in maxEmails" :key="i">
        <div class="form-group">
        <input :id="'address' + i" type="email" v-model="newEmails[i-1]" style="text-align: center; border-radius: 25px;" class="form-control" >
        </div>
      </div>

      <button type="submit">Add Email</button>

      <p v-if="errorMessage">{{ errorMessage }}</p>
    </form>
  </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      emails: [],
      newEmails: [],
      maxEmails: 5,
      errorMessage: '',
      successMessage: null,
    };
  },
  mounted() {
    this.fetchEmails();
  },
  methods: {
    handleLogout() {
      localStorage.clear();
      window.location.href = '/';
    },
    welcomepage() {
        window.location.href = '/welcome';
    },
    async callApi() {
      const username = localStorage.getItem('username');
      const password = localStorage.getItem('password');
      const level = localStorage.getItem('level');

      const apiUrl = 'http://127.0.0.1:3000/generate-pdf';
      const encodedCredentials = btoa(`${username}:${password}`);
      const headers = { 'Authorization': `Basic ${encodedCredentials}` };
      try {
        const response = await axios.post(apiUrl, {level}, { headers });
        console.log(response.data);
        alert("Email Sent Successfully")
      } catch (error) {
        console.error(error);
        alert("Please add recipient Email Addresses to send report")
      }
    },
    fetchEmails() {
      const username = localStorage.getItem('username');
      const password = localStorage.getItem('password');

      const apiUrl = 'http://127.0.0.1:3000/get-recipient';
      const encodedCredentials = btoa(`${username}:${password}`);
      const headers = { 'Authorization': `Basic ${encodedCredentials}` };

      axios.get(apiUrl, { headers })
        .then(response => {
          this.emails = response.data;
          if (this.emails.length > 0) {
            for (let i = 0; i < this.emails.length && i < this.maxEmails; i++) {
              this.newEmails[i] = Object.assign(this.emails[i]);
            }
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    addEmail() {
      const username = localStorage.getItem('username');
      const password = localStorage.getItem('password');

      const apiUrl = 'http://127.0.0.1:3000/insert-recipient';
      const encodedCredentials = btoa(`${username}:${password}`);
      const headers = { 'Authorization': `Basic ${encodedCredentials}` };

      if (this.emails.length < this.maxEmails) {
        const newEmails = this.newEmails;
        axios.post(apiUrl, newEmails, { headers })
          .then(response => {
            console.log(response.data);
            alert("Email added successfully!");
          })
          .catch(error => {
            console.log(error);
          });
          // this.successMessage = "Email added successfully!";
      } else {
        this.errorMessage = `You can only add up to ${this.maxEmails} email addresses.`;
      }
    }
  }
}
</script>

<style>
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

.page-title {
  background-color: #007bff;
  color: #d56363;
  padding: 10px 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80px;
}

.email-container {
    max-width: 500px;
    margin: 0 auto;
    padding: 50px;
}

.form-group {
    margin-bottom: 20px;
    width: 95%;
    text-align: center; 
    border-radius: 25px;
  }

.email-list {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: black;
  color: white;
  overflow: hidden;
}

.email-list video {
  position: fixed;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  z-index: -1;
  transform: translateX(-50%) translateY(-50%);
}

button {
    padding: 10px 20px;
    margin-top: 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:focus {
    outline: none;
  }
</style>
