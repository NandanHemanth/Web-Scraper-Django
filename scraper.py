from bs4 import BeautifulSoup
import requests

# URL from indeed.com for keyword 'Python Developer'
url = "https://www.indeed.com/jobs?q=Python+developer"

# Sending a GET request to the web page to get the DNS response
response = requests.get(url)

# Parsing the contents using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

print(soup)