from llama_index.llms.groq import Groq
from llama_index.core.workflow import Context
from tavily import AsyncTavilyClient

from dotenv import load_dotenv
import os
import logging
logging.basicConfig(level=logging.INFO)

load_dotenv()
GROQ_API = os.getenv("GROQ_API")
tavily  = os.getenv("TAVILY")


class LLM:
    logging.info("Loading LLM configuration")
    def __init__(self):
        logging.info("Initializing LLM Model")
        try:
            self.llm = Groq(
                model = "llama-3.2-1b-preview",
                api_key = GROQ_API,
                is_function_calling_model= True,
            )
        except Exception as e:
            logging.error(f"Error in initializing LLM model: {e}")


class Utils:
    def __init__(self):
        logging.info("Initializing Utils")

    async def search_web(query:str)-> str:
        """
        useful for using the web to answer the queries
        """
        client = AsyncTavilyClient(api_key=tavily)
        return str(await client.search(query))
    
    async def record_notes(ctx: Context, notes:str, notes_title:str,) -> str:
        """
        useful for recording the notes
        """
        current_states = await ctx.get("state")
        if "research_notes" not in current_states:
            current_states["research_notes"] ={}
        current_states["research_notes"][notes_title] = notes
        await ctx.get("state", current_states)
        return "Notes recorded successfully"
    
    
