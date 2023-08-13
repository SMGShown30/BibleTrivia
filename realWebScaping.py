from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text



soup = BeautifulSoup(html_text, "lxml")

print(soup)

jobs = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")
for job in jobs:
    comp_name = job.find("h3", class_ = "joblist-comp-name").text.replace(" ", "")
    skills = job.find("span", class_ = "srp-skills").text.replace(" ", "").replace(",", ", ")



    #print(f"""
    #Company Name: {comp_name.strip()}
   # Required Skills: {skills.strip()}
    #""")


