# Import the BeautifulSoup Library
from bs4 import BeautifulSoup
# Import the URL Library
import urllib
# Import the CSV library to export as a CSV file
# import csv
baseURL = 'https://www.splcenter.org/fighting-hate/hate-incidents?keyword=&page='

for count in range(228):
	# print url
	# Load in and read the URL
	url = baseURL + str(count + 1)
	# print(url)
	r = urllib.urlopen(url).read()
	# Pass the HTML from the URL into BeautifulSoup
	soup = BeautifulSoup(r)

	# print(soup.findAll('li', attrs={'class': 'views-row'}))

	# Loop through all the HTML data and pull out the important information using the specific labels and IDs
	for text in soup.findAll('li', attrs={'class': 'views-row'}):
		date = text.find('span', attrs={'class': 'date-display-single'}).get_text()
		taxonomy = text.find('div', attrs={'class': 'field-name-field-hate-incident-type'}).find('div', attrs={'class': 'field-item'}).get_text()
		location = text.find('div', attrs={'class', 'field-name-field-state'}).find('div', attrs={'class': 'field-item'}).get_text()
		long_text = text.find('div', attrs={'class', 'field-name-field-long-text'}).find('div', attrs={'class': 'field-item'}).get_text()
		print("'" + date + "'," + taxonomy + ",'" + location + "','" + long_text + "'")
	    
	    # Write all the data to the CSV file
	    # csv_writer.writerow([station_lat, station_lon])