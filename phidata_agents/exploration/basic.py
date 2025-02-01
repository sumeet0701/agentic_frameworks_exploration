from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API = os.getenv("GROQ_API")

agent = Agent(
    model = Groq(
        id = "llama-3.2-1b-preview",
        api_key= GROQ_API,
    ),
    description = f"""
You are a Quantitative analyst with expert in trading and you task is to response the query that is only related to finance else 
responed with:  your query has been forwarded to respective agent wait for the her response.
""",
    markdown= False,\
    # debug_mode= True
)

while True:
    input_text = input("Enter your query string: \n\n")
    if input_text == "exit":
        break
    agent.print_response(input_text)