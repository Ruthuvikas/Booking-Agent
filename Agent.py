from langgraph.graph import StateGraph, START, END
from utils.state import AgentState
from langgraph.prebuilt import tools_condition
from langgraph.prebuilt import ToolNode
from utils.nodes import chat, tools
from langgraph.checkpoint.memory import MemorySaver

graph_builder = StateGraph(AgentState)
graph_builder.add_node("chatbot", chat)
graph_builder.add_node("tools", ToolNode(tools))
graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges(
"chatbot",
tools_condition,
)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge("chatbot", END)
memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)
thread = {"configurable": {"thread_id": "1"}}
while True:
  user_input=input("User: ")
  if user_input.lower() in ["quit","q"]:
    print("Good Bye")
    break
  for event in graph.stream({'messages':("user",user_input)}, thread):
    for key, value in event.items():
      if key == "chatbot" and isinstance(value.get('messages'), list) and value['messages']:
        print("Assistant:", value['messages'][0].content)
