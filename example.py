import requests
from bs4 import BeautifulSoup
import csv

def job_scraping():

    URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=USA'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='ResultsContainer')
    #print(results.prettify())
    job_elems = results.find_all('section', class_='card-content')

    return job_elems


def store_jobs(job_elems, file_path):

    with open(file_path, 'w+') as outcsv:   

        writer = csv.writer(outcsv, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(['title', 'company', 'location'])
            
        for job_elem in job_elems:
        
            title_elem = job_elem.find('h2', class_='title')
            company_elem = job_elem.find('div', class_='company')
            location_elem = job_elem.find('div', class_='location')
            if None in (title_elem, company_elem, location_elem):
                continue
            
            print(title_elem.text.strip())
            print(company_elem.text.strip())
            print(location_elem.text.strip())
            print()

            writer.writerow([
                str(title_elem.text.strip()), 
                str(company_elem.text.strip()), 
                str(location_elem.text.strip())
            ])


if __name__ == '__main__':

    job_elems = job_scraping()
    
    file_path = 'results.csv'
    store_jobs(job_elems, file_path)
