# Import the BeautifulSoup Library
from bs4 import BeautifulSoup
# Import the URL Library
import urllib
# Import the CSV library to export as a CSV file
import csv
import re

main_url = 'http://www.accuweather.com/en/us/new-york-ny/10007/month/349727?monyr='
month = '12'
day_url = '/01/'
year = '2014'

# Load in and read the URL
r = urllib.urlopen(main_url + month + day_url + year).read()
# Pass the HTML from the URL into BeautifulSoup
soup = BeautifulSoup(r)

# Write the CSV file (pass in a file name and the 'w' stands for write)
with open('Desktop/weather-' + month + '-' + year + '.csv', 'w') as csvfile:
	csv_writer = csv.writer(csvfile)

    # Write headers to the CSV file
	csv_writer.writerow(['day', 'temp'])

	# Loop through all the HTML data and pull out the important information using the specific labels and IDs
	for link in soup.findAll('div', attrs={'class': 'box'}):
	    day = link.find('h3', attrs={'class': 'date'}).get_text()
	    day_num = re.sub('[^0-9]', '', day)
	    temp = link.find('div', attrs={'class': 'info'}).find('div', attrs={'class': 'actual'}).find('span', attrs={'class': 'temp'}).get_text()
	    temp_num = re.sub('[^0-9]', '', temp)
	    
	    # Write all the data to the CSV file
	    csv_writer.writerow([month + "/" + day_num + "/" + year, temp_num])