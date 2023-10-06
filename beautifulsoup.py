import requests
#allow user to obtain html code
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
#page contain a response element here 200, that significates the page was found(famous response is 404 for error 404 if page is not found)
soup = BeautifulSoup(page.content, 'html.parser')
#allow user to obtain html code,html parser is a parser included in python

class_name="gem-c-document-list__item-description"
#only if there is a class description into the tag
description=soup.find_all("p",class_=class_name)

#here is how to create a list
description_content=[]
for descr in description:
    description_content.append(descr.string)

print (description_content)