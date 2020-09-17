# import requests 
# # from bs4 import BeautifulSoup 
# import csv 
# from pprint import pprint
import bs4 as bs

import sys
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
print('sdsd')

class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()



    # page = Page('https://pythonprogramming.net/parsememcparseface/')
    # soup = bs.BeautifulSoup(page.html, 'html.parser')
    # js_test = soup.find('p', class_='jstest')

print('sd')
URL = 'https://in.tradingview.com/symbols/NSE-POWERGRID/'
page = Page(URL)
soup = bs.BeautifulSoup(page.html, 'html.parser')
# soup = bs.BeautifulSoup(source, 'lxml')

# soup = BeautifulSoup(r.content, 'html5lib') 
print(soup)
table = soup.find('div', attrs = {'class':'tv-widget-fundamentals__item'}) 

print(table)
table = soup.find_all('table', attrs = {'id':'equityInfo'})
print(table)