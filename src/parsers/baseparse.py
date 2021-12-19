from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
import pandas
from operator import itemgetter

class BaseParser(object):
    def __init__(self, link, debugmode=False):
        self.header={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        self.baseURL=link

    def encode_URL(self):
        self.encodedURL=self.baseURL+"?"+urlencode(self.params)
    
    def getHTML(self):
        response = requests.get(website, headers=headers)
        webpage = response.content
        self.soup = BeautifulSoup(webpage, "html.parser")

    def parse(self):
        _set_link(self, )


parse = BaseParser("link.org")