# 1. Import the necessary LIBRARIES
import requests
from bs4 import BeautifulSoup
import pandas
from operator import itemgetter
import csv
from datetime import datetime

import pandas as pd

# 2. Create a User Agent (Optional)
headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 ("
                         "KHTML, like Gecko) Version/4.0 Safari/534.30"}

def stepstoneparse(website):
    response = requests.get(website, headers=headers)
    webpage = response.content
    soup = BeautifulSoup(webpage, "html.parser")
    articles = soup.find_all('article')
    page_jobs=[]
    for job in articles:
        job_title = job.find(attrs={"data-at" : "job-item-title"}).text
        link = job.find(attrs={"data-at" : "job-item-title"})["href"]
        company = job.find(attrs={"data-at" : "job-item-company-name"}).text
        job_id = job["id"]
        page_jobs.append([job_id ,job_title, company, link])
    return page_jobs

#stepstoneparse("https://www.stepstone.de/5/ergebnisliste.html?what=data%20engineer&where=Deutschland&radius=0&searchOrigin=Homepage_top-search&of=0")

run=0
jobs=[]
link="https://www.stepstone.de/5/ergebnisliste.html?what=data%20engineer&where=Deutschland&radius=0&searchOrigin=Homepage_top-search&of={}"
with open ("output/jobs.csv", "a", encoding="utf-8", newline="") as jobfile, open ("output/log.csv", "a", encoding="utf-8") as logfile:
    while True:
        parselink=link.format(run*25)
        logfile.write(str(datetime.now())+" - parsing link "+parselink+"\n")
        tmp=stepstoneparse(parselink)
        if (not tmp):
            break
        print(len(tmp))
        #jobs+=tmp
        writer = csv.writer(jobfile)
        writer.writerows(tmp)
        print("parsed {} jobs".format((run+1)*25))
        run+=1
    
#df=pd.DataFrame.from_records(jobs,columns=["id", "title", "company", "link"])
#df["link"]=df["link"].apply(lambda x: "stepstone.de"+x)
#df.to_csv("output/jobs.csv", index=False, sep=";", encoding="utf-8-sig")

