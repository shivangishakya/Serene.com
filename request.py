import requests, base64

url = 'http://localhost:3000/predict'

username = '310'
password = 'absd'

# Encode the username and password in base64
credentials = f'{username}:{password}'
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Add the Authorization header to the request
headers = {'Authorization': f'Basic {encoded_credentials}'}


r = requests.post(url, headers=headers, json={'Student ID': 14,'Academics': 1,'Looks_Fitness':0,'Social_life':1,'Xtra_curricular':0,'Athletics':0,'Career':0,'Finance':0,'Relationship':0,'Cultural_Shock':0,'Emotional_bullied':0,'Physical_bullied':0,'Verbal_bullied':0,'Social_bullied':0,'Cyber_bullied':0,'International':1,'Miss_home':1,'Family_friends':1,'Food':0,'Sensory':0,'Miss_social':0,'Native_language':0,'Courses':0,'Loan':1,'Stressed_commute':0,})
print(r.json())