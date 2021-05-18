import requests
from bs4 import BeautifulSoup

URL = 'https://ie.indeed.com/jobs?q=&l=Ireland'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

job_elems = soup.find_all('div', 'jobsearch-SerpJobCard')


for job_elem in job_elems:
    
    title = job_elem.find('h2', class_ = 'title')

    company = job_elem.find('span', class_ = 'company')
    if None in company:
        continue

    location = job_elem.find('span',class_ = 'location')
    if None in location:
        continue

    if "new" in title.text:
        title.text.replace("new", "")

    print(title.text.strip())
    print(location.text.strip())
    print(company.text.strip())
    print()

