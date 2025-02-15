from custom_agents.web_search_agent import WebSearchAgent
from rich.console import Console
from rich.markdown import Markdown
console = Console()
# Initialize the agent once, outside the loop
web_search_agent = WebSearchAgent([])
conversation_history = []

while True:
    input_text = input("Enter your query string: \n\n")
    console.print(Markdown(f"**User:** {input_text}"))
    if input_text == "exit":
        break

    conversation_history.append({"role": "user", "content": input_text})
    # Update the conversation history in the existing agent
    web_search_agent.query = input_text
    response = web_search_agent.web_search_agent()

    conversation_history.append({"role": "assistant", "content": response})
    console.print(Markdown(f"**Assistant:** {response}"))
    console.print("-"*100)



