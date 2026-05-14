from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import time
# Website URL
url = "https://robotronix.co.in/"
# Start browser
driver = webdriver.Chrome()
# Open website
driver.get(url)
# Wait for page to load
time.sleep(5)
# Get page source
html = driver.page_source
# Parse HTML
soup = BeautifulSoup(html, "html.parser")
# Metadata
metadata = {
    "title": soup.title.string if soup.title else "No Title",
    "url": url
}
# Headings
headings = []
for tag in soup.find_all(["h1", "h2", "h3"]):
    headings.append({
        "tag": tag.name,
        "text": tag.get_text(strip=True)
    })
# Sections / paragraphs
sections = []
for p in soup.find_all("p"):

    text = p.get_text(strip=True)

    if text:
        sections.append(text)
# Final JSON
data = {
    "metadata": metadata,
    "headings": headings,
    "sections": sections
}
# Print JSON
print(json.dumps(data, indent=4))
# Close browser
driver.quit() 

