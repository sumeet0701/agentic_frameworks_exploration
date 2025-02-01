from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API = os.getenv("GROQ_API")

# we search agent using the duckduckgo
web_search_agent = Agent(
    name= "web_search_agent",
    role="Search the web for News, Infromation",
    model = Groq(
        id = "llama-3.2-1b-preview",
        api_key= GROQ_API,
    ),
    tools= [DuckDuckGoTools()],
    instructions="Always include source",
    description= "Your are expert in searching the News, Infromation and sentiment of the company in market.",
    show_tool_calls= True,
    debug_mode=True,


)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model = Groq(
        id = "llama-3.2-1b-preview",
        api_key= GROQ_API,
    ),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions="Use tables to display data",
    description= "Your task is to scrape the data for the following companies that is provided by the user",
    show_tool_calls=True,
    markdown=True,
    debug_mode= True
)


agent_team = Agent(
    team= [finance_agent, web_search_agent],
    show_tool_calls= True,
    markdown= True,
    debug_mode=True,
    description=f"""
Role: Quantitative Analyst with expert in creating the Trading strategies using News, and companies information.
your task is to create the Trading strategies for the provided company name provide by the user and you can ask the user to about senarios for 
your reference that will help to generate the Trading strategies.
""",

)
