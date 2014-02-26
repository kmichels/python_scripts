from urllib import urlopen
from bs4 import BeautifulSoup
import ystockquote

optionsUrl = 'http://finance.yahoo.com/q/op?s=AAPL&m=2014-04'
optionsPage = urlopen(optionsUrl)
optionssoup = BeautifulSoup(optionsPage)

# create a list of all the table rows that have the corresponding attrs
optionsTable = [
	[x.text for x in y.parent.contents]
	for y in optionssoup.find_all('td', attrs={'class': 'yfnc_h', 'nowrap': ''})
]

# last item in list is gibberish: kill it with fire
del optionsTable[-1]

# now clear out all the call options

for item in optionsTable:
	if 'C' not in item[1]:
		print item


# This probably needs to be a function
# Code to get the "current" stock price

print ("Apple stock price is currently %s." % (ystockquote.get_price('AAPL')))
