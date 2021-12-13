import requests
from bs4 import BeautifulSoup
import pandas
from operator import itemgetter

class StepstoneParser(BaseParser):
    def __init__ (self, search:str, location:str, radius:int):
        self.link = "https://www.stepstone.de/5/ergebnisliste.htm"
        self.params = {
            "what": search,
            "where": location,
            "radius": radius
        }
        super(StepstoneParser, self).generate_start_link(params)

    def parse(self):
        response = requests.get(website, headers=headers)
        webpage = response.content
        soup = BeautifulSoup(webpage, "html.parser")
        articles = soup.find_all('article')
        page_jobs=[]
        for job in articles:
            job_title = job.find(attrs={"data-at" : "job-item-title"}).text
            link = job.find(attrs={"data-at" : "job-item-title"})["href"]
            company = job.find(attrs={"data-at" : "job-item-company-name"}).text
            job_id = job["id"]
            page_jobs.append([job_id ,job_title, company, link])
        return page_jobs