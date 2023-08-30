import requests
from bs4 import BeautifulSoup
import pymongo

# Define the URL for the job listings page
url = "https://www.indeed.com/jobs?q=Python+developer"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Extract job listings (modify this part based on the actual HTML structure)
job_listings = []
for listing in soup.find_all("div", class_="jobsearch-SerpJobCard"):
    title = listing.find("h2", class_="title").text.strip()
    company = listing.find("span", class_="company").text.strip()
    location = listing.find("div", class_="location").text.strip()
    job_listings.append({"title": title, "company": company, "location": location})

# for job in job_listings:
#     print(job)

# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Specify the database and collection
db = client["job_listings"]
collection = db["python_developer"]

# Insert the scraped job listings into the collection
for job in job_listings:
    collection.insert_one(job)

# Close the MongoDB connection
client.close()
