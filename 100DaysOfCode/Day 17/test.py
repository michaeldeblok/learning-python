import requests
import json

list = "https://opentdb.com/api.php?amount=30&category=15&difficulty=easy&type=boolean"
response = requests.get(list)
# print(response)
print(response.content.results) # Return the raw bytes of the data payload
# print(response.text) # Return a string representation of the data payload
# print(response.json) # This method is convenient when the API returns JSON


Q_LOCATION = ['results', 0, 'question']
CA_LOCATION = ['results', 0, 'correct_answer']
WA_LOCATION1 = ['results', 0, 'incorrect_answers', 0]
WA_LOCATION2 = ['results', 0, 'incorrect_answers', 1]
WA_LOCATION3 = ['results', 0, 'incorrect_answers', 2]

response = requests.get('https://opentdb.com/api.php?amount=30&category=15&difficulty=easy&type=boolean').text
response_info = json.loads(response)
question_list = response_info['results']

question_bank = []
for question in question_list:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    #new_question = Question(question_text, question_answer)
    #question_bank.append


