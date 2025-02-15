from agents.web_search_agent import WebSearchAgent


web_search_agent = WebSearchAgent()


conversation_history = []
while True:
    input_text = input("Enter your query string: \n\n")
    conversation_history.append({"role": "user", "content": input_text})
    if input_text == "exit":
        break
    response = web_search_agent.web_search_agent(input_text)
    conversation_history.append({"role": "assistant", "content": response})
    
    print(response)
    print("-"*100)



