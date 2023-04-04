<template>
  <div>
    <div class="page-title" :style="{ backgroundColor: backgroundColor }">
      <h2>{{ survey.title }}</h2>
    </div>
    <div class="survey-container">
      <div v-if="!completed">
        <div v-for="(question, index) in survey.questions" :key="index" class="question">
          <h3>{{ question.text }}</h3>
          <ul>
            <li v-for="(option, optionIndex) in question.options" :key="optionIndex" @click="respondToQuestion(index, optionIndex)">
              <input v-if="question.type === 'radio'" type="radio" :id="'option-' + index + '-' + optionIndex" :name="'question-' + index" :value="optionIndex" :checked="question.response === optionIndex">
              <input v-else type="checkbox" :id="'option-' + index + '-' + optionIndex" :value="optionIndex" v-model="question.response">
              <label :for="'option-' + index + '-' + optionIndex" :style="{ color: textColor }">{{ option.text }}</label>
            </li>
          </ul>
        </div>
        <button type="button" @click="submitSurvey" :style="{ backgroundColor: buttonColor }">Submit Survey</button>
      </div>
      <div v-else>
        <h3>Thank you for your response!</h3>
      </div>
    </div>
  </div>
</template>

<script>
const axios = require('axios');

export default {
  data() {
    return {
      survey: {
        title: 'Calculate Your Stress in Few Minutes',
        questions: [
          {
            text: 'Ques 1: Primary Reasons of Stress (You can select multiple options)',
            type: 'checkbox',
            options: [
              { text: 'Academic pressure (exam, assignments, projects)' },
              { text: 'Good looks and fitness' },
              { text: 'Social Life' },
              { text: 'Busy with extra-curricular activities' },
              { text: 'Athletic performance' },
              { text: 'Career development and job search' },
              { text: 'Financial stress' },
              { text: 'Relationship' },
              { text: 'Cultural shock (New place, new people)' },
              { text: 'No Stress' }
            ],
            response: []
          },
          {
            text: 'Ques 2: Have you been bullied? Select the reasons.',
            type: 'checkbox',
            options: [
              { text: 'Mentally/emotionally bullied' },
              { text: 'Physically bullied' },
              { text: 'Verbal bullying' },
              { text: 'Social bullying (humiliation, spreading rumors)' },
              { text: 'Cyber bullying (inappropriate comments in social media)' },
              { text: 'No bullying' },
            ],
            response: []
          },
          {
            text: 'Ques 3: Are you an International Student?',
            type: 'radio',
            options: [
              { text: 'Yes' },
              { text: 'No' },
            ],
            response: []
          },
          {
            text: 'Ques 4: What do you miss the most about your home?',
            type: 'checkbox',
            options: [
              { text: "No, I don't miss my home" },
              { text: 'Yes, Family and friends' },
              { text: 'Yes, Food' },
              { text: 'Yes, Sensory experience of staying in home' },
              { text: 'Yes, Social life of my hometown' },
              { text: 'Yes, Native language conversations' }
            ],
            response: []
          },
          {
            text: 'Ques 5: How many courses you have taken?',
            type: 'radio',
            options: [
              { text: '1' },
              { text: '2' },
              { text: '3' },
              { text: '4' },
              { text: 'More than 4' },
            ],
            response: null
          },
          {
            text: 'Ques 6: Financing the education',
            type: 'radio',
            options: [
              { text: 'Student Loan' },
              { text: 'Self financed' },
            ],
            response: null
          },
          {
            text: 'Ques 7: Is your commute to college stressful?',
            type: 'radio',
            options: [
              { text: 'Yes' },
              { text: 'No' },
              { text: 'Maybe' },
            ],
            response: null
          },
        ]
      },
      completed: false,
      backgroundColor: '#f2f2f2',
      textColor: '#333',
      buttonColor: '#007bff'
    }
  },
  methods: {
    respondToQuestion(questionIndex, optionIndex) {
      if (this.survey.questions[questionIndex].type === 'radio') {
        this.survey.questions[questionIndex].response = optionIndex
      }
    },
    async submitSurvey() {
      const selectedOptions = this.survey.questions.map(question => {
    if (question.type === 'checkbox') {
      return question.options.filter((option, index) => question.response.includes(index)).map(option => option.text);
    } else {
      return question.options[question.response].text;
    }
  });

  console.log(selectedOptions);
  this.completed = true;

  const username = localStorage.getItem('username');
  const password = localStorage.getItem('password');

  const apiUrl = 'http://127.0.0.1:3000/api/surveys';
  const encodedCredentials = btoa(`${username}:${password}`);
  const headers = { 'Authorization': `Basic ${encodedCredentials}` };

  axios.post(apiUrl, { selectedOptions }, { headers })
  .then(response => {
    // Handle the API response
    console.log(response.data);
    this.completed = true;
    this.$router.push({ name: "Result" });
  })
  .catch(error => {
    // Handle the API error
    console.error(error);
  });
    }
  }
}
</script>

<style scoped>
.page-title {
  background-color: #007bff;
  color: #d56363;
  padding: 10px 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80px;
}

.survey-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 300vh;
  text-align: left;
  max-height: calc(230vh - 30px); /* subtract the height of the page-title and button */
  overflow-y: auto; /* enable vertical scrolling when content exceeds max-height */
}

.question {
  margin-bottom: 20px;
  margin-left: 1rem;
  padding: 5px 20px;
}

h3 {
  margin-bottom: 10px;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
  
  li {
    margin-bottom: 10px;
    cursor: pointer;
  }
  
  input[type="radio"],
  input[type="checkbox"] {
    margin-right: 10px;
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
  