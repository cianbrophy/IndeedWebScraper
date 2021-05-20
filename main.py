import requests
from bs4 import BeautifulSoup

## function to find jobs
def findJobs(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    job_elems = soup.find_all('div', 'jobsearch-SerpJobCard')


    for job_elem in job_elems:
    
        title = job_elem.find('h2', class_ = 'title')

        company = job_elem.find('span', class_ = 'company')
        if company is None:
                continue

        location = job_elem.find('span',class_ = 'location')
        if location is None:
            continue


        print("Job Title: " + title.text.strip())
        print("Location: " + location.text.strip())
        print("Company Name: " + company.text.strip())
        print()

def main():
    keyword = input("Enter any keywords (jobs, title, company etc.):\n")
    location = input("Enter your preferred location:\n")

    URL = 'https://ie.indeed.com/jobs?q=' + keyword + '&l=' + location + ''

    print(URL)

    findJobs(URL)

    pageNumber = 10

    nextPage = None
    isFinished = False
    
    while isFinished == False:
        
        nextPage = input("Would you like to view another page? (Yes/No)\n").lower()

        if nextPage == "yes":
            URL += "&start=" + str(pageNumber)
            pageNumber + 10
            findJobs(URL)

        if nextPage == "no":
            isFinished == True
            break
        else:
            print("Invalid command entered, please enter Yes/No")


if __name__ == '__main__':
    main()
