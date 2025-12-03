from utils import state
from langchain_openai import ChatOpenAI
from utils.tools import flight_search, hotel_search, general_search

tools = [flight_search, hotel_search, general_search]

def chat(state):
    model = ChatOpenAI(temperature=0.2, model_name="gpt-4o")
    model = model.bind_tools(tools, parallel_tool_calls=False)
    import logging
    logging.info("Chat function called")
    system_prompt = """You are a friendly Travel Booking assistant. Focus on finding the best deals and providing personalized recommendations."""
    messages = state["messages"]
    messages = [{"role": "system", "content": system_prompt}] + messages
    response = model.invoke(messages)
    return {"messages": [response]}