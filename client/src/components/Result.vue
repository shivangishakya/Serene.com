<template>
    <div>
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
          <li v-for="item in response" :key="item.id">{{ item.title }}</li>
        </ul>
      </div>
      <h1>Bar Graph:</h1>
      <div>
        <canvas ref="chart"></canvas>
      </div>
      <h1>YouTube Videos:</h1>
      <div class="video-grid">
        <div v-for="(video, index) in videos" :key="index" class="video-item">
          <h3>{{ video.title }}</h3>
          <div class="video-wrapper">
          <iframe width="560" height="315" :src="video.url" frameborder="0" allowfullscreen></iframe>
        </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { Chart } from 'chart.js';
  
  export default {
    name: 'ApiBarGraphAndVideo',
    data() {
      return {
        loading: true,
        error: null,
        response: null,
        videos: [
          {
            title: 'Video 1',
            url: 'https://www.youtube.com/embed/QpYrV-f_2Ng'
          },
          {
            title: 'Video 2',
            url: 'https://www.youtube.com/embed/bsVlTy3GaJo'
          },
          
        ]
      };
    },
    mounted() {
      axios.get('http://127.0.0.1:3000/')
        .then(response => {
          this.loading = false;
          this.response = response.data;
          this.createBarGraph();
        })
        .catch(error => {
          this.loading = false;
          this.error = error.message;
        });
    },
    methods: {
      createBarGraph() {
        const chartData = {
          labels: this.response.map(item => item.title),
          datasets: [
            {
              label: 'API Data',
              data: this.response.map(item => item.value),
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1
            }
          ]
        };
        const chartOptions = {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        };
        new Chart(this.$refs.chart, {
          type: 'bar',
          data: chartData,
          options: chartOptions
        });
      }
    }
  };
  </script>

<style>
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


  