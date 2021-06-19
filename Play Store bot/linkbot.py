import requests
import urllib
from bs4 import BeautifulSoup
url = 'https://play.google.com/store/search?q='
f = open("App names.txt", 'r')
g = open('Link.txt' , 'w')
for line in f:
	tempURL = url + urllib.parse.quote(line.strip()) + '&c=apps'
	res = requests.get(tempURL)
	soup = BeautifulSoup(res.text, 'html.parser')
	link = soup.select('#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > div:nth-child(1) > c-wiz > div > div > div.uzcko > div > div > a')
	print(line)
	try:
		g.write(line + ':  https://play.google.com' + link[0].get('href') + '\n')
	except:
		g.write(line + 'failed\n')
		continue
g.close()
f.close()
