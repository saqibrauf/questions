import requests, json
from bs4 import BeautifulSoup


home_url = 'http://localhost:8000/brainly-last-q/'
response = requests.post(home_url)
data = response.json()
counter = data['lastq']
counter = int(counter) + 1

def add_question(url, counter):
	url = 'https://brainly.com/question/' + str(counter)
	response = requests.get(url)
	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'html.parser')
		category = soup.find_all('li', class_='sg-breadcrumb-list__element')[1].get_text()
		question = soup.find('div', class_='js-question-content')
		question = question.find('h1').get_text()
		
		answer = soup.find('div', attrs={ 'data-test' : 'answer-content'})
		if answer == 'None':
			answer = 'Not Answered Yet'

		data = {
			'category' : category,
			'source' : 'brainly',
			'source_id' : str(counter),
			'question' : question.strip(),
			'answer' : str(answer),
		}

		r = requests.post('http://localhost:8000/add-question/', data=data)
		r = r.json()
		print(r['message'])

	else:
		print('Not Found')

	counter = int(counter) + 1
	url = 'https://brainly.com/question/' + str(counter)
	add_question(url, counter)



url = 'https://brainly.com/question/' + str(counter)
add_question(url, counter)