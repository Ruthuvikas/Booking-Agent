from langchain_core.tools import tool
from serpapi import GoogleSearch
import os

@tool
def flight_search(departure_id: str, arrival_id: str, outbound_date: str, return_date: str) -> dict:
    """Search for flight tickets with given parameters
    
    Args:
        departure_id: Airport code for departure (e.g., 'CDG')
        arrival_id: Airport code for arrival (e.g., 'AUS')
        outbound_date: Departure date in YYYY-MM-DD format
        return_date: Return date in YYYY-MM-DD format
        
    Returns:
        dict: Flight search results
    """
    params = {
        "engine": "google_flights",
        "hl": "en",
        "gl": "us",
        "departure_id": departure_id,
        "arrival_id": arrival_id,
        "outbound_date": outbound_date,
        "return_date": return_date,
        "currency": "USD",
        "api_key": os.getenv("SERPAPI_API_KEY")
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()
    
    return {
        "flight_details": results,
        "departure": departure_id,
        "arrival": arrival_id,
        "outbound_date": outbound_date,
        "return_date": return_date
    }
    # return {
    #     "departure": "CDG",
    #     "arrival": "AUS",
    #     "outbound_date": "2024-12-24",
    #     "return_date": "2024-12-30"
    # }