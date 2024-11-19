# CS361_NameLookupService

This project is a Flask-based API that retrieves name-related information using the [Behind the Name API](https://www.behindthename.com/api/) and returns a formatted response to the client.

## Features

- **Retrieve Name Information**: Queries the Behind the Name API for details about a name.
- **Consolidates by Gender**: Groups the data by gender (`m`, `f`, `mf`, etc.).
- **Formatted Output**: Returns the name, gender, and associated usage information in a readable format.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-repository-name.git
cd project
```
### 2. Install Dependencies
Ensure you have Python 3.8+ installed. Install the required packages:
```bash
pip install -r requirements.txt
```
### 3. Configure the API Key
Add your Behind the Name API key in config.py:
```python
API_KEY = "your_api_key_here"
```
### 4. Run the Server
Start the server by running:
```bash
python run.py

```
## Usage

### API Endpoints
### 1. Home Route
- URL: `/`
- Method: `GET`
- Description: Returns a simple message indicating the server is running. 
### 2. Name Info Route
- URL:  `/name-info`
- Method: `GET`
- Query Parameters:
  - `name`: The name to query (e.g., `?name=Jamie`
- Response: Consolidated name data grouped by gender.
### Requesting Data
To request data from the microservice, send an HTTP `GET` request to the `/name-info` endpoint with the query parameter `name`.
```python
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
```
### Receiving Data
The response from the microservice will be plain text in the following format:
```makefile
Name: <name>
Gender: <gender>
Usage: <comma-separated usage list>
```

## Usage Example

### Example Request
```bash
curl "http://127.0.0.1:5000/name-info?name=Jamie"
```
### Example Response
```makefile
Name: Jamie
Gender: mf
Usage: English, Scottish
```

## UML Sequence Diagram
![image](https://github.com/user-attachments/assets/03291ec0-75c9-4274-8bc8-ddb5ada12dab)
