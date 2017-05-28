# coding = utf-8
import urllib
import urllib.request
import re
import os
from bs4 import BeautifulSoup
def getWord(url,index):
	bs = getH(url,index)
	tables = bs.find('table',class_='table-bordered')
	trs = tables.findAll('tr',class_='row')
	dict = {}
	for tr in trs:
		word = tr.find('td',class_='span2').string
		ex = tr.find('td',class_='span10').string
		dict.setdefault(word,ex)
	return dict

def getH(url,index):
	newUrl = url + index
	print(newUrl)
	data = urllib.request.urlopen(newUrl).read()
	data = data.decode('utf-8')
	bs = BeautifulSoup(data)
	return bs
rootUrl = 'https://www.shanbay.com/'
url = 'https://www.shanbay.com/wordbook/182800/'
data = urllib.request.urlopen(url).read()
data = data.decode('utf-8')
bs = BeautifulSoup(data)
trs = bs.findAll('td',class_='wordbook-wordlist-name')
for tr in trs:
	a = tr.find('a')
	print(a)
	h = a['href']
	for i in range(1,11):
		index = h+'/?page='+str(i)
		d = getWord(rootUrl,index)
		s = str(d).replace('\\n','')
		d = eval(s)
		keys = list(d.keys())
		with open('H:1.txt','a') as f:
			for key in keys:
				f.write(key+':'+d.get(key)+'\n');
			

	
