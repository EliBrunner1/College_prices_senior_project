import requests

API_KEY = 'HRnr80yWE4NsBtYUorM2hHu1EAhRYIIRJpqZ7eDa'
API_URL = "https://api.data.gov/ed/collegescorecard/v1/schools"  # Specify the correct endpoint

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    print("API call successful!")
    print(response.content.decode())  # Print the actual data
else:
    print(f"Error: {response.status_code}")
