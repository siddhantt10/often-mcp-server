# main.py
from mcp.server.fastmcp import FastMCP
from typing import List, Dict, Any, Optional
import requests
from pydantic import BaseModel, Field

# Create an MCP server
mcp = FastMCP("Demo")


#API endpoint URL
API_URL = "https://often-task.onrender.com/recommended/"

# Function to fetch travel recommendations from API
def get_travel_recommendations(nights: int) -> List[Dict[str, Any]]:
    try:
        # Make GET request to the API endpoint with nights parameter
        response = requests.get(API_URL, params={"nights": nights})
        # Check if request was successful (status code 200)
        if response.status_code == 200:
            return response.json()  # Return JSON response as Python dict
        else:
            return []  # Return empty list if request fails
    except Exception as e:
        print(f"Error fetching travel recommendations: {e}")
        return []  # Return empty list on exception

# Add a travel recommendation tool MCP server
@mcp.tool()
def recommend_travel(nights: int) -> List[Dict[str, Any]]:
    """
    Makes a request to the travel recommender API and returns trip recommendations.
    
    Args:
        request: The request containing the number of nights for the trip.
        
    Returns:
        A response containing a list of recommended trips.
    """
    return get_travel_recommendations(nights)



# tester
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

