from textwrap import dedent
from typing import Iterator
from agno.agent import Agent
from agno.agent import RunResponse
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.utils.log import logger
from custom_agents.prompt import web_search_prompt
from dotenv import load_dotenv

import os


load_dotenv()
GROQ_API = os.getenv("GROQ_API")

class WebSearchAgent:
    def __init__(self, query):
        logger.info("Initializing WebSearchAgent")
        self.query = query

    def web_search_agent(self):
        logger.info(f"web Searching your: {self.query}")
        try:
            self.web_search_agent = Agent(
                model=Groq(
                    id="deepseek-r1-distill-qwen-32b",    
                    api_key=GROQ_API),
                debug_mode= True,
                markdown= False,
                description= web_search_prompt,
                tools=[DuckDuckGoTools(), Newspaper4kTools()],
                
            )
            response =  self.web_search_agent.print_response(self.query)
            return response
        
            
        except Exception as e:
            logger.error(f"Error in web_search_agent: {e}")
            raise e
    
    def run(self) -> Iterator[RunResponse]:
        logger.info(f"Running web_search_agent: {self.query}")
        inital_response: RunResponse = self.web_search_agent.run(self.query)
        if inital_response is None or not inital_response.content:
            yield RunResponse(
                run_id= self.run_id,
                content= "No response from the web_search_agent",

            )
            return
        
        
        

        