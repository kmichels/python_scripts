from urllib import urlopen
from bs4 import BeautifulSoup

optionsUrl = 'http://finance.yahoo.com/q/op?s=AAPL&m=2014-04'
optionsPage = urlopen(optionsUrl)
soup = BeautifulSoup(optionsPage)

optionsTable = [
	[x.text for x in y.parent.contents]
	for y in soup.find_all('td', attrs={'class': 'yfnc_h', 'nowrap': ''})
]

for item in optionsTable:
	print item
