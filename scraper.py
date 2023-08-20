from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests

# URL from indeed.com for keyword 'Python Developer'
url = "https://www.indeed.com/jobs?q=Python+developer"

# MongoDB configuration
client = MongoClient("mongodb://localhost:27017/")
db = client["job_listings"]
collection = db["python_developer"]

# Sending a GET request to the web page to get the DNS response
response = requests.get(url)

# Parsing the contents using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
#print(soup)

# Find all job listings on the page
job_listings = soup.find_all("div", class_="jobsearch-SerpJobCard")

# Loop through each job listing to extract the data
for job in job_listings:
    title = job.find("h2", class_ = "title").text.strip()
    company = job.find("span", class_ = "company").text.strip()
    location = job.find("div", class_ = "recJobLoc")["data-rc-loc"]

    print(title, company, location)

    # Inserting scraped Data into MongoDB
    job_data = {
        "title": title,
        "company": company,
        "location": location
    }
    collection.insert_one(job_data)

    print("Title : ", title)
    print("Company : ", company)
    print("Location : ", location)
    print("=" * 30)

client.close()