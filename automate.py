from pprint import pprint
import bs4 as bs
import openpyxl
import sys
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
print('loaded all modules')


class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self.on_load_finished)
        self.load(QUrl(url))
        self.triggerAction(QWebEnginePage.ReloadAndBypassCache, True)
        self.app.exec_()

    def on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()


URL = 'https://in.tradingview.com/symbols/NSE-MRPL/'
page = Page(URL)
soup = bs.BeautifulSoup(page.html, 'html5lib')

#-----------------------------------------------------------------------------
# EPS, MarketCap, DividendYield, P.E
table = soup.find_all('div', attrs = {'class':'tv-category-header__fundamentals js-header-fundamentals'}) 
d1 = {}  # dictionary having EPS, MarketCap, DividendYield, P.E, SharePrice

try:
    for i in table[0].contents[1:]:
        d1[i.contents[3].contents[0]] = i.contents[1].contents[0]

    print(d1)
except:
    print('Error while calculating EPS, Div, PE !')
# pprint(d1)
#------------------------------------------------------------------------------

# Share Price
table = soup.find_all('div', attrs = {'class':'tv-symbol-price-quote__value js-symbol-last'})

try:
   d1['SharePrice'] = table[0].contents[0].contents[0]

except:
    print('Error while calculating Share price !')

# pprint(d1)
#------------------------------------------------------------------------------

table = soup.find_all('div', attrs = {'class':'tv-widget-fundamentals tv-widget-fundamentals--card-view'})
d2 = {}
table = table[0].contents
# print(table) 
try:
    for i in table:
        try:

            for j in i.contents:
                try:
                    d2[j.span.contents[0].strip()] = j.span.nextSibling.nextSibling.contents[0].strip()
                except:
                    pass
        except:
            pass
    print(d2)
except:
    print('Error while calculating all the values !')
    