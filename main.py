import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_base = os.getenv('OPENAI_API_BASE')
openai.api_type = 'azure'
openai.api_version = '2022-12-01'

deployment_id = os.getenv('OPENAI_API_DEPLOYMENT_ID')

print('Sending a test completion job')
myprompt = 'Tell me what is the capital city of Spain'
response = openai.Completion.create(engine=deployment_id, prompt=myprompt, max_tokens=100)
text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
print("Response Text is: " + text)

print(response)