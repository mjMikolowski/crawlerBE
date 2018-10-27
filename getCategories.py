#!/usr/bin/env python
import urllib.request
import lxml.html
import random
import io
from lxml.etree import tostring
from six.moves.html_parser import HTMLParser

def getSite(url):
    return urllib.request.urlopen(url)

if __name__ == '__main__':
	category = 2
	categories = io.open("categories.csv", mode="w", encoding="utf-8")
	
	categories.write("Aktywny (0/1); Nazwa; Kategoria nadrzędna; Kategoria główna; Przypisany URL\n")
	
	content = getSite("https://biurwa.pl/").read()
	site = lxml.html.fromstring(content)
	
	listaKategorii = site.xpath("//ul[@class='menu sf-menu sf-js-enabled sf-shadow main'][1]")
	listaKategorii = listaKategorii[0]
	catNr = 0
	for mainCat in listaKategorii:
		catLinks = mainCat.xpath("./a[1]/@title")
		for links in catLinks:
			catNr = catNr + 1
			if (catNr < 3):
				continue
			urlLink = links.lower()
			urlLink = urlLink.replace(" ", "_")
			urlLink = urlLink.replace('ą', 'a')
			urlLink = urlLink.replace('ć', 'c')
			urlLink = urlLink.replace('ę', 'e')
			urlLink = urlLink.replace('ł', 'l')
			urlLink = urlLink.replace('ń', 'n')
			urlLink = urlLink.replace('ó', 'o')
			urlLink = urlLink.replace('ś', 's')
			urlLink = urlLink.replace('ź', 'z')
			urlLink = urlLink.replace('ż', 'z')
			categories.write("1;"+links+";Strona główna;0;"+urlLink+"\n")
			category = category + 1
	
	
	categories.close()