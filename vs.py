import requests
from bs4 import BeautifulSoup

# Load the HTML content from the file
with open('vs.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table in the HTML
table = soup.find('table', {'class': 'table'})

# Initialize an empty list to store the dictionaries
schools_list = []

# Iterate over each row in the table body
for row in table.find('tbody').find_all('tr'):
    # Extract the columns in the row
    columns = row.find_all('td')

    # Extract the necessary information
    name = columns[0].get_text(strip=True)
    address = columns[1].get_text(strip=True)
    google_map = columns[1].find('a')['href']
    phone = columns[3].get_text(strip=True)
    url = columns[0].find('a')['href']

    # Create a dictionary for the current school
    school_dict = {
        'school_name': name,
        'address': address,
        'google_map': google_map,
        'phone': phone,
        'website': url
    }

    # Add the dictionary to the list
    schools_list.append(school_dict)

# Print the list of dictionaries
for school in schools_list:
    print(str(school) + ",")