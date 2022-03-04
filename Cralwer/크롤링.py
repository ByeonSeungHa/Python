from bs4 import BeautifulSoup
import urllib.request as req

res = req.urlopen('http://localhost:5500')
soup = BeautifulSoup(res, 'html.parser')
soup.select()