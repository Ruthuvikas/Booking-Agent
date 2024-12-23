from langchain_core.tools import tool

@tool
def book():
    """Book Flight ticket
    """
    return "Booking confirmed"