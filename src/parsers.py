from abc import ABC, abstractmethod
from urllib.parse import urlencode
import logging
import csv
import pandas as pd
import concurrent.futures

from helper import retrieve_website
from jobs import StepstoneJob

class BaseParser(ABC):
    def __init__(self, max_threads):
        self.jobs = []
        self._create_startinglink()
        self._thread_executor = concurrent.futures.ThreadPoolExecutor(max_workers = max_threads)

    @abstractmethod
    def parse(self):
        """subclasses must implement the parse method
        """        
        pass

    def _create_startinglink(self):
        """creates the startinglink to begin parsing this method gets calls from contructor, so make sure to have param-dictionary created before calling the method.
        """        
        self._startinglink = self._generate_page_link()

    def _generate_page_link(self, page_keyword:str = None, page:str = None):
        """creates url by encoding search_param dictionary and optionally the pageinformation into the link

        Args:
            page_keyword (str, optional): specify an optional attribute name. Must me given if the page is given, otherwise it will be ignored. Defaults to None.
            page (str, optional): the pageparameter value that should be encoden into the url. Defaults to None.

        Returns:
            str: the encoded url
        """        
        if (page_keyword and page):
            self.search_params[page_keyword] = page
        param_encoding=urlencode(self.search_params)
        return f"{self.rootlink}?{param_encoding}"

    def to_json(self, file):
        """exports the parsed information to a json file

        Args:
            file (str): path of the json file
        """        
        ls_jobs = map(lambda job: job.to_list(), self.jobs)
        df = pd.DataFrame.from_records(ls_jobs)
        with open(file, "w", encoding = 'utf-8') as output_file:
            df.to_json(output_file, orient = "records")

    

    def _add_job(self, job_url, job_id = None, job_title = None, job_company = None):
        """adds a job the the joblist

        Args:
            job_url (str): url of the job the
            job_id (str, optional): id of the job. Defaults to None.
            job_title (str, optional): the title of the job. Defaults to None.
            job_company (str, optional): the company name. Defaults to None.
        """        
        self.jobs.append(StepstoneJob(job_url, job_id, job_title, job_company))


class StepstoneParser(BaseParser):
    def __init__(self, search, location, radius, max_threads):
        """Create a StepstoneParser

        Args:
            search (str): searchstring used for the search on the jobsite
            location (str): city or country of the location the job will be searched in
            radius (int): the radius of the location
            max_threads(int): the maximum amount of threads running in parallel
        """        
        self.rootlink = "https://www.stepstone.de/5/ergebnisliste.html"
        self.search_params = {
            "what": search,
            "where": location,
            "radius": radius
        }
        super().__init__(max_threads)

    def parse(self):
        run_count = 0
        
        pages = []
        for i in range(2):
            pages.append(self._generate_page_link(page_keyword = "of", page = str(i * 25)))
        for page in pages:
            self._thread_executor.submit(StepstoneParser.__parse_stepstone_page(self, page))
        print("starting multithread-parseing")
        #self._thread_executor.map(StepstoneParser.__parse_stepstone_page, pages)

        print("beginning enrichment")
        for job in self.jobs:
            job.parse()

    def __parse_stepstone_page (self, link):
        """Parses a stepstonepage an adds it to the joblist.

        Args:
            link (str): link of the stepstone webpage

        Returns:
            int: returns -1 if there are no jobs on the page, returns 1 if jobs where found
        """        
        soup = retrieve_website(link)
        articles = soup.find_all('article')
        if (not articles):
            return -1
        for job in articles:
            job_title = job.find(attrs={"data-at" : "job-item-title"}).text
            link = "https://www.stepstone.de/"+job.find(attrs={"data-at" : "job-item-title"})["href"]
            company = job.find(attrs={"data-at" : "job-item-company-name"}).text
            job_id = job["id"]
            self._add_job(link, job_id, job_title, company)
        return 1
