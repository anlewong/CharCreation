from bs4 import BeautifulSoup
import requests

barb = requests.get("http://dnd5e.wikidot.com/barbarian")
pageinfo = barb.headers
print(pageinfo)
#soup = BeautifulSoup(pageinfo, 'html.parser')
#print(soup.prettify())