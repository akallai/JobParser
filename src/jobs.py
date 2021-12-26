from abc import ABC, abstractmethod

from helper import retrieve_website

class Job(ABC):

    def __init__(self, job_link, job_id = None, job_title = None, job_company = None,  introduction = "", description = "", profile = "", offer = ""):
        """Create a Job.

        Args:
            job_link (str): the url of the job, which contains the job content.
            job_id (str, optional): the id of the job, the website uses. Defaults to None.
            job_title (str, optional): The title of the job. Defaults to None.
            job_company (str, optional): The company behind the job. Defaults to None.
            introduction (str, optional): introduction to the job/company. Defaults to "".
            description (str, optional): Jobdescription. Defaults to "".
            profile (str, optional): Profile the company is looking for. Defaults to "".
            offer (str, optional): Offerings of the company regarding the job. Defaults to "".
        """                
        self.link = job_link
        self.id = job_id
        self.title = job_title
        self.company = job_company
        self.introduction = introduction
        self.description = description
        self.profile = profile
        self.offer = offer

    @abstractmethod
    def parse(self):
        """A job subclass must implement the parse method.
        """        
        pass

    def to_list(self):
        """Converts the job into a list.

        Returns:
            list: List containing all of the job information
        """        
        return [self.link, self.id, self.title, self.company, self.introduction, self.description, self.profile, self.offer]


class StepstoneJob(Job):
    def __init__(self, job_link, job_id = None, job_title = None, job_company = None):
        super().__init__(job_link, job_id, job_title, job_company)


    def parse(self):
        soup = retrieve_website(self.link)
        try:
            introduction=soup.find("section", attrs={"class": "at-section-text-introduction"})
            introduction=introduction.text
            self.introduction = introduction
        except Exception:
            pass
        try:
            description=soup.find("section", attrs={"class": "at-section-text-description"})
            description=description.text
            #Überschrift entfernen
            description=description[description.find("\n")+1:]
            self.description = description
        except Exception:
            pass
        try:
            profile=soup.find("section", attrs={"class": "at-section-text-profile"})
            profile=profile.text
            #Überschrift entfernen
            profile=profile[profile.find("\n")+1:]
            self.profile = profile
        except Exception:
            pass
        try:
            offer=soup.find("section", attrs={"class": "at-section-text-weoffer"})
            offer=offer.text
            #Überschrift entfernen
            offer=offer[offer.find("\n")+1:]
            self.offer = offer
        except Exception:
            pass
        return self