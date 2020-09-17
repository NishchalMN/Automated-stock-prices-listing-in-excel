# import requests 
# from bs4 import BeautifulSoup 
# import csv 
# from pprint import pprint
# import bs4 as bs


   
# URL = "https://in.tradingview.com/symbols/NSE-POWERGRID/"
# r = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"}) 

# soup = BeautifulSoup(r.content, 'html5lib') 
    
# table = soup.find_all('div', attrs = {'class':'tv-widget-fundamentals__row'}) 

# for i in table:
#     print(i)
# Library for opening url and creating 
# requests 
import urllib.request 

# pretty-print python data structures 
from pprint import pprint 

# for parsing all the tables present 
# on the website 
from html_table_parser import HTMLTableParser 

# for converting the parsed data in a 
# pandas dataframe 
import pandas as pd 


# Opens a website and read its 
# binary contents (HTTP Response Body) 
def url_get_contents(url): 

	# Opens a website and read its 
	# binary contents (HTTP Response Body) 

	#making request to the website 
	req = urllib.request.Request(url=url) 
	f = urllib.request.urlopen(req) 

	#reading contents of the website 
	return f.read() 

# defining the html contents of a URL. 
xhtml = url_get_contents('https://www.moneycontrol.com/india/stockpricequote/power-generationdistribution/powergridcorporationindia/PGC').decode('utf-8') 

# Defining the HTMLTableParser object 
p = HTMLTableParser() 

# feeding the html contents in the 
# HTMLTableParser object 
p.feed(xhtml) 

# Now finally obtaining the data of 
# the table required 
pprint(p.tables) 

# converting the parsed data to 
# datframe 
print("\n\nPANDAS DATAFRAME\n") 
print(pd.DataFrame(p.tables[1]))
