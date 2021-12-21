from abc import ABC, abstractmethod

from helper import retrieve_website

class Job(ABC):

    def __init__(self, job_link, job_id = None, job_title = None, job_company = None):
        self.link = job_link
        self.id = job_id
        self.title = job_title
        self.company = job_company

    @abstractmethod
    def parse(self):
        pass

    def to_list(self):
        return [self.link, self.id, self.title, self.company]


class StepstoneJob(Job):
    def __init__(self, job_link, job_id = None, job_title = None, job_company = None):
        super().__init__(job_link, job_id, job_title, job_company)

    def parse(self):
        print("enrichment")
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