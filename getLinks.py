#!/usr/bin/env python
import urllib.request
import lxml.html

def getSite(url):
    return urllib.request.urlopen(url)

if __name__ == '__main__':
	links = open("tmp.txt", 'w')
	for i in range (1, 240):
		search_site = getSite("https://biurwa.pl/szukaj/-?p="+str(i)).read()
		site = lxml.html.fromstring(search_site)
		prod = site.xpath("//table[@class='mpc']")
		for pr in prod:
			pr2 = pr.xpath("tr/td[@class='name']/div/h2/a/@href")
			for p2 in pr2:
				links.write('https://biurwa.pl'+p2+'\n')
	links.close()