from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('https://www.linkedin.com/vsearch/p?keywords=Journalist&openAdvancedForm=true&locationType=I&countryCode=us&rsid=152764351433515470607&orig=MDYS').read()
soup = BeautifulSoup(r)
print(soup.prettify())

# type = soup.find('h2').findAll('a').find('href')

for country in soup.findAll('div', attrs={'class': 'options-dropdown'}):
    code = country.find('select').findAll('option').get('value')
    print(code)
    # countries = urllib.urlopen('https://www.linkedin.com/vsearch/p?keywords=Journalist&openAdvancedForm=true&locationType=I&countryCode=' + code + '&rsid=152764351433515470607&orig=MDYS').read()
    # soup2 = BeautifulSoup(countries)
    # for count in soup2.findAll('div', attrs={'class': 'search-info'}):
    #     print(count.find('h1').get_text() + ',' + link2.find('div').get_text())

