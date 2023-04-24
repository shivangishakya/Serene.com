<template>
    <div>
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
        <div class="video-container">
        <video autoplay loop muted>
          <source src="../assets/result.mp4" type="video/mp4">
        </video>
      </div>
      <h1>Your Stress Level:</h1>
      <p v-if="loading">Loading data...</p>
      <div v-else>
        <p v-if="error">{{ error }}</p>
        <ul v-else>
          <h1>{{ String(parseInt(responseData.level) * 100/5) + "% corresponds to level: " + responseData.level }}</h1>
        </ul>
      </div>
      <div class="chart-container">
        <canvas ref="chart"></canvas>
      </div>
      <div class="description">
          <p>"It is impossible to live without failing at something unless you live so 
            cautiously that you might as well not have lived at all, in which case you
             have failed by default." - J. K. Rowling</p>
          <p>
            Don’t dwell on the past or think too much about the future. 
            There are times when it is nice to reminisce or when it is important 
            to make plans for our future, but one of the best ways to stop worrying 
            is to take things one day at a time. Practice mindfulness to increase your
             self-awareness and improve your psychological well-being by becoming more
              present in your own environment. Living in the present will help you 
              cherish each moment and make the most of your day.
          </p>
          </div>
      <h1>Suggested Videos:</h1>
      <div class="video-grid">
        <div v-for="(video, index) in videos" :key="index" class="video-item">
          <div class="video-wrapper">
          <iframe width="560" height="315" :src="video.url" frameborder="0" allowfullscreen></iframe>
        </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import Chart from 'chart.js/auto';

  
  export default {
    name: 'ApiBarGraphAndVideo',
    data() {
      return {
        error: null,
        loading: true,
        responseData: {},
        chartResponse: {},
        videos: [
          {
            title: 'Video 1',
            url: 'https://www.youtube.com/embed/QpYrV-f_2Ng'
          },
          {
            title: 'Video 2',
            url: 'https://www.youtube.com/embed/bsVlTy3GaJo'
          },
          {
            title: 'Video 3',
            url: 'https://www.youtube.com/embed/o0j9WlLhceM'
          },
          
        ],
        chart: null
      };
    },
    created() {
    const username = localStorage.getItem('username');
    const password = localStorage.getItem('password');

    // API call for response data
    const apiUrl = 'http://127.0.0.1:3000/predicted-val';
    const encodedCredentials = btoa(`${username}:${password}`);
    const headers = { 'Authorization': `Basic ${encodedCredentials}` };
    axios.get(apiUrl, { headers })
      .then(response => {
        this.loading = false;
        this.responseData = response.data;
        localStorage.setItem('level', this.responseData.level);
        localStorage.setItem('prevlevel', this.responseData.prevlevel);
        console.log("HELLO: ", this.responseData.level, this.responseData.prevlevel)
      })
      .catch(error => {
        this.loading = false;
        this.error = error.message;
      });
    },
    mounted() {
      this.drawBarChart();
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
        alert("Please go Back->Add Recipient and add recipient Email Addresses")
      }
    },
      drawBarChart(){
        const level = localStorage.getItem('level');
        const prevlevel = localStorage.getItem('prevlevel');
        console.log("HELLO1: ", level, prevlevel)

        if (typeof Chart !== 'undefined') {
          const ctx = this.$refs.chart.getContext('2d');
          this.chart = new Chart(ctx, {
            type: 'bar',
            data: {
              labels: ['Previous Stress', 'Current Stress'],
              datasets: [{
                label: 'Stress Levels',
                data: [prevlevel, level],
                backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)'],
                borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)'],
                borderWidth: 1
              }]
            },
            options: {
              scales: {
              y: {
                beginAtZero: true,
                ticks: {
                  precision: 0,
                  stepSize: 5
                }
              }
            }
          }
          });
        } else {
          console.log('Chart.js is not defined');
        }
      }
    },
  };
</script>


<style>
    .description {
    background-color: white;
    text-align: center;
    padding: 2rem;
    border-radius: 100rem;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    margin-top: 2rem;
    margin-left: 10%;
    max-width: 80%;
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

.chart-container {
  width: 50%;
  margin: 0 auto;
}

.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  grid-gap: 20px;
}

.video-item {
  padding-left: 40px;
}

.video-card {
  border: 1px solid #ccc;
  padding: 20px;
}

.video-wrapper {
  position: relative;
  padding-bottom: 56.25%;
  /* 16:9 aspect ratio */
  height: 0;
}

.video-wrapper iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 90%;
  height: 90%;
}
</style>


  