# For general python dataFrame manipulation, aggregations, and plots.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# For handling API calls. 
from pprint import pprint
# For user-friendly data file access.
import os
import shutil
import requests

api_key = "HRnr80yWE4NsBtYUorM2hHu1EAhRYIIRJpqZ7eDa"

# Base URL for the College Scorecard API
base_url = "https://api.data.gov/ed/collegescorecard/v1/schools?"

# Set query parameters (e.g., state, degree level)
params = {
    'school.state': 'OR',  # Filter by state (Oregon)
    'school.degrees_awarded.predominant': '2,3',  # Associate's or Bachelor's degrees
    'api_key': api_key
}

# Make the API request
response = requests.get(base_url, params=params)

# Parse the JSON data
data = response.json()


# Extract the names from the data

for school in data['results']:
    school_name = school.get('school').get('name')
    school_state = school.get('school').get('state')
    instate_tution = school.get('latest').get('cost').get('tuition').get('in_state')
    outstate_tution = school.get('latest').get('cost').get('tuition').get('out_of_state')

print(school_name)
print(school_state)
print(instate_tution)
print(outstate_tution)
