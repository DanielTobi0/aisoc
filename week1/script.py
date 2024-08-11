"""Build a simple LLM application"""

import groq
import os
from dotenv import load_dotenv
load_dotenv()


GROP_API_KEY = os.environ.get("GROQ_API_KEY")
groq_client = groq.Groq(api_key = GROP_API_KEY)

sys_prompt = """You are a helpful virtual assistance. \
    Your goal is to provide useful and relevant \
        responses to my query"""

models = [
    "llama-3.1-405b-reasoning",
    "llama-3.1-70b-versatile",
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]


def generate(model, query, temperature):
    response = groq_client.chat.completions.create(
        model = model,
        messages = [
            {'role': 'system', 'content': sys_prompt},
            {'role': 'user', 'content': query},
        ],
    response_format = {'type': 'text'},
    temperature = temperature

)
    answer = response.choices[0].message.content
    return answer

if __name__ == '__main__':
    query = 'in 100 words tell me about yourself'
    model = models[1]
    temperature = 0.2
    print(generate(model, query, temperature))