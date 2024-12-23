from langgraph.graph import StateGraph, START, END
from utils.state import AgentState
from langgraph.prebuilt import tools_condition
from langgraph.prebuilt import ToolNode
from utils.nodes import chat, tools

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

graph = graph_builder.compile()

while True:
  user_input=input("User: ")
  if user_input.lower() in ["quit","q"]:
    print("Good Bye")
    break
  for event in graph.stream({'messages':("user",user_input)}):
    for value in event.values():
      print("Assistant:",value["messages"][0].content)