from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
import pandas
from operator import itemgetter

class BaseParser(object):
    def __init__(link, self):
        self.header={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        self.link=link

    def encode_link(self, params: dict):
        self.encodedlink=baselink+"?"+urlencode(params)
    
    def getHTML(self):
        response = requests.get(website, headers=headers)
        webpage = response.content
        self.soup = BeautifulSoup(webpage, "html.parser")

    def parse(self):
        _set_link(self, )