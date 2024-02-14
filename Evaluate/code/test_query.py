import openai
from openai_cost_tracker import query_openai

openai.api_key = ""

prompt = "Hello World!"  # your prompt here

response = query_openai(
    model= "gpt-3.5-turbo-1106",
    messages=[{'role': 'user', 'content': prompt}],
    max_tokens=5,
    # rest of your OpenAI params here ...
    simulation=True,  # set to True to test the cost of a request without actually sending it to OpenAI
    print_cost=True   # set to True to print the cost of each request
)

print(response["choices"][0]["message"]["content"])
