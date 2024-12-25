from utils import state
from langchain_openai import ChatOpenAI
from utils.tools import flight_search, hotel_search, general_search

tools = [flight_search, hotel_search, general_search]

def chat(state):
    model = ChatOpenAI(temperature=0, model_name="gpt-4o")
    model = model.bind_tools(tools, parallel_tool_calls=False)
    system_prompt = """Be a helpful Travel Booking assistant"""
    messages = state["messages"]
    messages = [{"role": "system", "content": system_prompt}] + messages
    response = model.invoke(messages)
    return {"messages": [response]}