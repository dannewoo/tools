# Import the BeautifulSoup Library
from bs4 import BeautifulSoup
# Import the URL Library
import urllib
# Import the CSV library to export as a CSV file
# import csv
year = ['2016','2015','2014','2013','2012','2011','2010','2009','2008'];
quarter = ['_4q.html','_3q.html','_2q.html','_1q.html']
baseUrl = 'https://www.rita.dot.gov/bts/sites/rita.dot.gov.bts/files/subject_areas/airline_information/passengers_denied_confirmed_space_report/';

arrayURLs = []

for y in year:
	for q in quarter:
		arrayURLs.append(baseUrl + y + '/html/' + y + q)

for url in arrayURLs:
	# print url
	# Load in and read the URL
	r = urllib.urlopen(url).read()
	# Pass the HTML from the URL into BeautifulSoup
	soup = BeautifulSoup(r)
	print(url)
	print('Carrier,Involuntary,Voluntary')
	count = 0
	# Loop through all the HTML data and pull out the important information using the specific labels and IDs
	for link in soup.findAll('tr'):
		if count > 0:
			carrier = link.findAll('td')[0].get_text().replace(',', '')
			involuntary = link.findAll('td')[6].get_text().replace(',', '')
			voluntary = link.findAll('td')[8].get_text().replace(',', '')
			print(carrier + "," + involuntary + "," + voluntary)
		count += 1

	    # Write all the data to the CSV file
	    # csv_writer.writerow([station_lat, station_lon])