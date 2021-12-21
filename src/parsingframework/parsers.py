from abc import ABC, abstractmethod
from urllib.parse import urlencode
import logging
import csv

from helper import retrieve_website
from jobs import StepstoneJob

class BaseParser(ABC):
    def __init__(self):
        self.jobs = []
        self._create_startinglink()

    @abstractmethod
    def parse(self):
        pass

    def _create_startinglink(self):
        self._startinglink = self._generate_page_link()

    def _generate_page_link(self, page_keyword:str = None, page:str = None):
        if (page_keyword and page):
            self.search_params[page_keyword] = page
        param_encoding=urlencode(self.search_params)
        return f"{self.rootlink}?{param_encoding}"

    def to_csv(self, file):
        ls_jobs = map(lambda job: job.to_list(), self.jobs)
        with open(file, "w", encoding = "utf-8", newline="") as f:
            writer = csv.writer(f, delimiter = ";")
            writer.writerows(ls_jobs)
    

    def _add_job(self, job_url, job_id = None, job_title = None, job_company = None):
        self.jobs.append(StepstoneJob(job_url, job_id, job_title, job_company))
        #logger.info(f"Added the job: {job_id}")


class StepstoneParser(BaseParser):
    def __init__(self, search, location, radius):
        self.rootlink = "https://www.stepstone.de/5/ergebnisliste.html"
        self.search_params = {
            "what": search,
            "where": location,
            "radius": radius
        }
        super().__init__()

    def parse(self):
        run_count = 0
        while True:
            print("parsing next 25")
            parselink=self._generate_page_link(page_keyword = "of", page = str(run_count * 25))
            #logger.info(f"started parsing {parselink}")
            tmp=self.__parse_stepstone_page(parselink)
            if (not tmp):
                break
            run_count+=1
        print("beginning enrichment")
        ls_joblist = map(lambda job: job.parse(), self.jobs)
        

    def __parse_stepstone_page (self, link):
        soup = retrieve_website(link)
        articles = soup.find_all('article')
        if (not articles):
            return None
        for job in articles:
            job_title = job.find(attrs={"data-at" : "job-item-title"}).text
            link = job.find(attrs={"data-at" : "job-item-title"})["href"]
            company = job.find(attrs={"data-at" : "job-item-company-name"}).text
            job_id = job["id"]
            self._add_job(link, job_id, job_title, company)
        return 1
