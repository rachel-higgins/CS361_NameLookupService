import requests

URL = "http://127.0.0.1:5000"

name = input("Enter a name: ")
response = requests.get(f"{URL}/name-info", params={"name": name})

if response.status_code == 200:
    # Handle plain text response
    print(f"\n{response.text}\n")
else:
    # Handle errors with status code and details
    print(f"Error: {response.status_code}\nDetails: {response.text}")
