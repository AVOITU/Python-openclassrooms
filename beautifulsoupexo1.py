import re
#serve after for search into the html code
from bs4 import BeautifulSoup

def soup_assignations():
#Obtains the BeautifulSoup object, the title, and the content of the h1 tag.
  with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

  title_class = soup.title.string
  print(title_class)
  h1_class = soup.h1.string
  print(h1_class)
  
  return soup

def product_lists(soup):
  #create a list of products found on the website
  product_class = soup.find_all('h2')
  product_list = []
  for product in product_class:
  #normal loop to obtain a list
    product_list.append(product.string)

  print(product_list)
  
def price_lists(soup):
  #Creates a list that contains only the price values from all the p tags.
  price_class = soup.find_all('p')
  euro_list = []
  dollar_list=[]
  for price in price_class:
    price_sentence=price.string
    result=re.search(r'\b\d+\b', price_sentence)
    if result:
      euro_list.append(f"{result.group()}€")
      #create a new list with dollar price
      dollar_price=int(result.group())*1.2
      dollar_list.append(f"{dollar_price}$")

  print(euro_list)
  print(dollar_list)

def description_lists(soup):
  #Creates a list that contains only the elements of product descriptions from all the p tags.
  description_class = soup.find_all('p')
  description_list = []
  for description in description_class:
    description_sentence=description.string
    search_word = "Description"
    result=re.search(rf'\b{search_word}\b', description_sentence)
    if result:
      description_list.append(description.string)

  print(description_list)

def main():
  soup=soup_assignations()
  product_lists(soup)
  price_lists(soup)
  description_lists(soup)

if __name__ == "__main__":
  main()