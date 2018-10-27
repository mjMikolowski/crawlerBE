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
	kategoriaNadrzedna = "Artykuły biurowe"
	urlNadrzedne = "https://biurwa.pl/artykuly-biurowe-o_c_74_1.html"


	categories = io.open("subcategories.csv", mode="w", encoding="utf-8")
	
	categories.write("Aktywny (0/1); Nazwa; Kategoria nadrzędna; Kategoria główna; Przypisany URL; URL zdjęcia\n")
	
	content = getSite(urlNadrzedne).read()
	site = lxml.html.fromstring(content)
	
	content = site.xpath("//div[@id='content']")	
	content = content[0]
	categoryBoxesImages = content.xpath("//table/tbody/tr/td/table/tbody/tr/td/a/img/@src")
	categoryBoxesNames = content.xpath("//table/tbody/tr/td/table/tbody/tr[2]/td/a/span/strong/text()")
	subcategoryNames = content.xpath("//table/tbody/tr/td/table/tbody/tr[3]")
	size = len(categoryBoxesNames)
	for i in range(0, size):
		urlLink = categoryBoxesNames[i].lower()
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
		urlLink = urlLink.replace(",", "")
		urllib.request.urlretrieve("https://biurwa.pl/"+str(categoryBoxesImages[i]), "img/"+urlLink+".jpg")
		categories.write("1;"+categoryBoxesNames[i]+";"+kategoriaNadrzedna+"; 0;"+urlLink+"; C:/xampp/htdocs/crawler/img/"+urlLink+".jpg\n")
		subcats = subcategoryNames[i]
		for subc in subcats:
			names = subc.xpath("./a/text()")
			for sName in names:
				urlLink = sName.lower()
				urlLink = urlLink.replace(" ", "_")
				urlLink = urlLink.replace(",", "")
				urlLink = urlLink.replace('ą', 'a')
				urlLink = urlLink.replace('ć', 'c')
				urlLink = urlLink.replace('ę', 'e')
				urlLink = urlLink.replace('ł', 'l')
				urlLink = urlLink.replace('ń', 'n')
				urlLink = urlLink.replace('ó', 'o')
				urlLink = urlLink.replace('ś', 's')
				urlLink = urlLink.replace('ź', 'z')
				urlLink = urlLink.replace('ż', 'z')
				categories.write("1;"+sName+";"+categoryBoxesNames[i]+"; 0;"+urlLink+";\n")
	
	categories.close()