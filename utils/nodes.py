from utils import state
from langchain_openai import ChatOpenAI
from utils.tools import book

tools = [book]

def chat(state):
    model = ChatOpenAI(temperature=0, model_name="gpt-4o")
    system_prompt = """Be a helpful Travel Booking assistant"""
    messages = state["messages"]
    messages = [{"role": "system", "content": system_prompt}] + messages
    response = model.invoke(messages)
    return {"messages": [response]}