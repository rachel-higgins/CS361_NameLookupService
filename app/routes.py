from flask import Blueprint, request
import requests
from app.utils import consolidate_data
from config import API_KEY, URL

# Create a blueprint for main routes
main = Blueprint("main", __name__)


@main.route("/")
def home():
    return "Server is running. Press Ctrl+C to terminate."


@main.route("/name-info", methods=["GET"])
def get_name():
    # Extract name from query parameters
    name = request.args.get("name")
    if not name:
        return "Error: Name parameter is required", 400

    # Call Behind the Name API
    response = requests.get(URL, params={"name": name, "key": API_KEY})

    # Check for successful response
    if response.status_code != 200:
        return f"Error: Failed to get name information. Details: {response.text}", 500

    # Extract JSON data
    data = response.json()
    if not data:
        return f"No data found for the name '{name}'", 404

    # Consolidate and format data
    result = consolidate_data(name, data)
    return result
