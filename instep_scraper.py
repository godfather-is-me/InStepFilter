import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import unicodedata
import re
import numpy as np
import csv


URL = "https://www.infosys.com/instep/internship/projects.html"

r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html.parser') 
   
# Dict to be converted to df
#print(soup)
majors = {}
links = soup.findAll('td',title="Academic Concentration")
links = links + soup.findAll('td',title="Academic concentration")
links2 = soup.findAll('td',title="Project Area")
links3 = soup.findAll('td',title="Duration (in weeks)")
links4 = soup.findAll('td',title="Description")

#print(links)
rows = []
i = 0

with open('instep.csv', 'w', newline='') as file:#Find all outbound links on succsesor pages and explore each one 
    writer = csv.writer(file)
    writer.writerow(["Academic Concentration","Project Area", "Duration","Description"])

    while(i<len(links)):
        writer.writerow([links[i].text,links2[i].text,links3[i].text,links4[i].text,])
        i = i+1
        
