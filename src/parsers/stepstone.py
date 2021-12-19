import requests
from bs4 import BeautifulSoup
import pandas
from baseparse import BaseParser




class StepstoneParser(BaseParser):
    def __init__ (self, search:str, location:str, radius:int, debugmode=False):
        super().__init__("https://www.stepstone.de/5/ergebnisliste.html")
        self.params = {
            "what": search,
            "where": location,
            "radius": radius
        }
        
        

    def parse(self):
        super().encode_URL()
        response = requests.get(self.encodedURL, headers=self.header)
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