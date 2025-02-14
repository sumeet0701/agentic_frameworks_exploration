from textwrap import dedent
from agno.agent import Agent
from agno.models import groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class WebSearchAgent(Agent):
    def __init__(self):
        pass

    def web_search_agent(self, query):
        try:
            pass
        except Exception as e:
            logger.error(f"Error in web_search_agent: {e}")
            return dedent(f"""
            I'm sorry, I couldn't find any information on that topic.
            Please try again with a different query.
            """
            )



