from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('https://gensummit2015.sched.org/directory/attendees/2#.VWuES9NViko').read()
soup = BeautifulSoup(r)
# print type(soup)

# type = soup.find('h2').findAll('a').find('href')

for link in soup.findAll('div', attrs={'class': 'sched-person'}):
    person = link.find('h2').find('a').get('href')
    r2 = urllib.urlopen('https://gensummit2015.sched.org' + person).read()
    soup2 = BeautifulSoup(r2)
    for link2 in soup2.findAll('div', attrs={'id': 'sched-page-me-profile'}):
        print(link2.find('h1').get_text() + ',' + link2.find('div').get_text())

