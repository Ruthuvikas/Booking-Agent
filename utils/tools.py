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

@tool
def hotel_search(location: str, check_in_date: str, check_out_date: str) -> dict:
    """Search for hotels with given parameters
    
    Args:
        location: Location or hotel name to search for (e.g., 'Bali Resorts')
        check_in_date: Check-in date in YYYY-MM-DD format
        check_out_date: Check-out date in YYYY-MM-DD format
        
    Returns:
        dict: Hotel search results
    """
    params = {
        "engine": "google_hotels",
        "q": location,
        "hl": "en",
        "gl": "us",
        "check_in_date": check_in_date,
        "check_out_date": check_out_date,
        "currency": "USD",
        "api_key": os.getenv("SERPAPI_API_KEY")
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()
    
    return {
        "hotel_details": results,
        "location": location,
        "check_in_date": check_in_date,
        "check_out_date": check_out_date
    }

@tool
def general_search(query: str, location: str = None) -> dict:
    """Perform a general Google search with given parameters
    
    Args:
        query: Search query string
        location: Optional location to focus search results (e.g., 'Austin, Texas')
        
    Returns:
        dict: Search results
    """
    params = {
        "engine": "google",
        "q": query,
        "hl": "en",
        "gl": "us",
        "google_domain": "google.com",
        "api_key": os.getenv("SERPAPI_API_KEY")
    }
    
    if location:
        params["location"] = location
    
    search = GoogleSearch(params)
    results = search.get_dict()
    
    return {
        "search_results": results,
        "query": query,
        "location": location
    }

