from textwrap import dedent
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools
from custom_agents.prompt import web_search_prompt
from dotenv import load_dotenv

import os

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


load_dotenv()
GROQ_API = os.getenv("GROQ_API")

class WebSearchAgent:
    def __init__(self, query):
        logger.info("Initializing WebSearchAgent")
        self.query = query

    def web_search_agent(self):
        logger.info(f"web Searching your: {self.query}")
        try:
            web_search_agent = Agent(
                model=Groq(
                    id="deepseek-r1-distill-qwen-32b",    
                    api_key=GROQ_API),
                debug_mode= True,
                markdown= False,
                description= web_search_prompt,
                tools=[DuckDuckGoTools(), Newspaper4kTools()],
                
            )

            response = web_search_agent.run(self.query)
            return response

            
        except Exception as e:
            logger.error(f"Error in web_search_agent: {e}")
            raise e
        

        