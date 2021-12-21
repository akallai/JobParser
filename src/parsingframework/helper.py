from bs4 import BeautifulSoup
import requests

def retrieve_website(url, headers=
                            {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 ("
                             "KHTML, like Gecko) Version/4.0 Safari/534.30"}
):
    response = requests.get(url, headers=headers)
    webpage = response.content
    return BeautifulSoup(webpage, "html.parser")