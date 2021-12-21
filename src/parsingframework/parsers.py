from abc import ABC, abstractmethod
from urllib.parse import urlencode
from helper import retrieve_website
import logging
from jobs import StepstoneJob

class BaseParser(ABC):
    def __init__():
        self.jobs=[]

    @abstractmethod
    def parse(self):
        pass

    def _create_startinglink(self):
        param_encoding=urlencode(self.search_params)
        self._startinglink=f"{self.rootlink}?{param_encoding}"

    def export_jobs(self):
        raise NotImplementedError
    

    def add_job(self,url):
        """Adds a new Job to the joblist

        Args:
            url (Union[str, list]): The url to the job that was found. Accepts a link as string or a list of strings.
        """
        if (isinstance(url, list)):
            for item in url:
                self.jobs.append(item)
        else:
            self.jobs.append(StepstoneJob(url))


class StepstoneParser(BaseParser):
    def __init__(self, search, location, radius):
        super(StepstoneParser).__init__()
        self.rootlink = "https://www.stepstone.de/5/ergebnisliste.html"
        self.search_params = {
            "what": search,
            "where": location,
            "radius": radius
        }
        self._create_startinglink()
    def parse(self):
        run_count = 0
        while True:
            parselink=link.format(run*25)
            logger.info(f"started parsing {parselink}")
            tmp=stepstoneparse(parselink)
            if (not tmp):
                break
            print(len(tmp))
            #jobs+=tmp
            writer = csv.writer(jobfile)
            writer.writerows(tmp)
            print("parsed {} jobs".format((run_count+1)*25))
            run_count+=1
        

