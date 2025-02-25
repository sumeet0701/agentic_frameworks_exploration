from llama_index.llms.groq import Groq
from dotenv import load_dotenv
import os
import logging
logging.basicConfig(level=logging.INFO)

load_dotenv()
GROQ_API = os.getenv("GROQ_API")


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



        