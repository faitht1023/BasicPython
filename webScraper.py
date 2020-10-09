#Created by Andrew Dunham
from urllib.request import urlopen
from bs4 import BeautifulSoup

quote_page = "https://www.uvic.ca/services/food/what/commons/index.php#day3menu"

page = urlopen(quote_page)

soup = BeautifulSoup(page, "html.parser")

name_box = soup.find ("ul", attrs={'class': 'menuList'})

name = name_box.text.strip() # strip() is used to remove starting and trailing
print (name)

# get the index price
#price_box = soup.find("div", attrs={"class":"price"})
#price = price_box.text
#print (price)
