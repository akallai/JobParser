import pandas as pd
from bs4 import BeautifulSoup
import requests

df=pd.read_csv("output/jobs.csv", header=None)

headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 ("
                         "KHTML, like Gecko) Version/4.0 Safari/534.30"}

#länge csv
print(len(df[0]))

#länge ohne duplikate
print(len(set(df[0])))

tmp=df.duplicated(subset=0, )
duplicates=tmp[tmp==True]

df=df.drop_duplicates(subset=0)

df.to_csv("output/cleaned.csv", sep=";", index=False, header=False, encoding="utf-8")

def parse_detail(stepstonewebsite:str):
    response = requests.get(stepstonewebsite, headers=headers)
    webpage = response.content
    soup = BeautifulSoup(webpage, "html.parser")

    introduction, description, profile, offer = "","","",""
    try:
        introduction=soup.find("section", attrs={"class": "at-section-text-introduction"})
        introduction=introduction.text    
    except Exception:
        print("no introduction found")
    try:
        description=soup.find("section", attrs={"class": "at-section-text-description"})
        description=description.text
        #Überschrift entfernen
        description=description[description.find("\n")+1:]
    except Exception:
        print("no description found")
    try:
        profile=soup.find("section", attrs={"class": "at-section-text-profile"})
        profile=profile.text
        #Überschrift entfernen
        profile=profile[profile.find("\n")+1:]
    except Exception:
        print("no profile found")
    try:
        offer=soup.find("section", attrs={"class": "at-section-text-weoffer"})
        offer=offer.text
        #Überschrift entfernen
        offer=offer[offer.find("\n")+1:]
    except Exception:
        print("no offer found")
    return introduction, description, profile, offer

with open ("output/details.csv", "a") as myfile:
    for index, row in df.iterrows():
        print("index: ", index)
        intro, descr, profile, offer = parse_detail("https://www.stepstone.de/"+row[3])
        myfile.write("||||".join([row[0],row[1], row[2], row[3], intro, descr, profile, offer])+";;;;")
        