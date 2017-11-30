# Import the BeautifulSoup Library
from bs4 import BeautifulSoup
# Import the URL Library
import urllib
# Import the CSV library to export as a CSV file
import csv
baseURL = "http://thefallen.militarytimes.com/search?home_state="
arrayURLs = [1,2,66,3,4,5,6,7,8,51,67,9,10,68,11,12,13,14,15,16,17,18,19,69,20,21,22,23,24,25,26,65,27,28,29,30,31,32,33,34,64,35,36,37,70,38,53,39,40,41,42,43,54,44,45,46,47,48,49,50]

with open('fallen-soldiers.csv', 'w') as csvfile:
	csv_writer = csv.writer(csvfile)
	csv_writer.writerow(['Fallen', 'State Number'])

	for n in arrayURLs:
		# print url
		# Load in and read the URL
		url = baseURL + str(n)
		# print(url)
		r = urllib.urlopen(url, "html.parser").read()
		# Pass the HTML from the URL into BeautifulSoup
		soup = BeautifulSoup(r)

		# Loop through all the HTML data and pull out the important information using the specific labels and IDs
		for link in soup.findAll('body'):
			if link.find('h2', attrs={'class': 'h2-size'}):
				number_value = link.find('h2', attrs={'class': 'h2-size'}).get_text()
			else:
				number_value = "0"
			# print(str(n) + "," + number_value)
		    
		    # Write all the data to the CSV file
			csv_writer.writerow([number_value, str(n)])