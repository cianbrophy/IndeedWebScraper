import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')


job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    print(job_elem, end='\n'*2)
    ##title_elem = job_elem.find('h2', class_ = 'title')
    ##info_elem = job_elem.find('div', class_ = 'sjcl')
    ##print(title_elem)
    ##print(info_elem)
    ##print()
