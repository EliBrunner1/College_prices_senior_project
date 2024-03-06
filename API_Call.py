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

# Extract relevant information and print
#for school in data['results']:
 #   school_name = school.get('school').get('name')
    #tuition_in_state = school.get('latest').get('cost').get('tuition').get('in_state')
    #tuition_out_of_state = school.get('latest').get('cost').get('tuition').get('out_of_state')
    
    #print(f"School Name: {school_name}")
    #print(f"Tuition (In-State): ${tuition_in_state}")
    #print(f"Tuition (Out-of-State): ${tuition_out_of_state}\n")


College_Search_list = []
# Extract the names from the data
for school in data['results']:
    school_name = school.get('school').get('name')
    if school_name:
        College_Search_list.append(school_name)

# Create an empty string to store the HTML
html_output = ""

# Iterate through the list of schools
for school in College_Search_list:
    # Format each school name into an <li> element
    li_element = f"<li><a href='#'>{school}</a></li>"
    # Append it to the HTML output
    html_output += li_element

# Print the complete HTML
print(html_output)
