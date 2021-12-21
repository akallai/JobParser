from abc import ABC, abstractmethod

class Job(ABC):

    def __init__(self, link):
        self.link=link


    @abstractmethod
    def parse(self):
        pass

class StepstoneJob(Job):

    def __init__(self, link):
        super(StepstoneJob).__init__(self, link)