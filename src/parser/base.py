from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
import pandas
from operator import itemgetter

class BaseParser:
    params={}
    baselink = ""
    encodedlink = ""

    headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 ("
                         "KHTML, like Gecko) Version/4.0 Safari/534.30"}

    def set_link(params: dict):
        self.encodedlink=baselink+"?"+urlencode(params)
    
    def get_link():
        return self.encodedlink
    
    def getHTML():
        response = requests.get(website, headers=headers)
        webpage = response.content
        self.soup = BeautifulSoup(webpage, "html.parser")