import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

class_name="gem-c-document-list__item-description"
description=soup.find_all("p",class_=class_name)

description_content=[]
for descr in description:
    description_content.append(descr.string)

print (description_content)