from textwrap import dedent
from agno.agent import Agent
from agno.models import groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools
from agents.prompt import web_search_prompt
from dotenv import load_dotenv

import os

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


load_dotenv()
GROQ_API = os.getenv("GROQ_API")

class WebSearchAgent:
    def __init__(self):
        logger.info("Initializing WebSearchAgent")
        pass

    def web_search_agent(self, query):
        logger.info(f"web Searching your: {query}")
        try:
            web_search_agent = Agent(
                model=groq(
                    model_name="llama3-8b-8192",
                    api_key=GROQ_API),
                debug_mode= True,
                markdown= False,
                description= web_search_prompt,
                tools=[DuckDuckGoTools(), Newspaper4kTools()],
                
            )

            response = web_search_agent.run(query)
            return response

            
        except Exception as e:
            logger.error(f"Error in web_search_agent: {e}")
            return dedent(f"""
            I'm sorry, I couldn't find any information on that topic.
            Please try again with a different query.
            """
            )