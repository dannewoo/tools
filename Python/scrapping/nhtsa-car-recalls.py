# Import the BeautifulSoup Library
from bs4 import BeautifulSoup
# Import the URL Library
import urllib

main_url = 'https://www.cars.com/recalls/'
brands = ['acura','audi','bmw','chevrolet','dodge','ford','gmc','honda','hyundai','infiniti','jeep','kia','lexus','mercedes_benz','mini','mitsubishi','nissan','subaru','toyota','volkswagen','volvo']

for b in brands:
	url = main_url + b
	# print url
	# Load in and read the URL
	r = urllib.urlopen(url).read()
	# Pass the HTML from the URL into BeautifulSoup
	soup = BeautifulSoup(r)

	# Loop through all the HTML data and pull out the important information using the specific labels and IDs
	for link in soup.findAll('body'):
		for r in link.findAll('div', attrs={'class', 'recallNumber'}):
			recallNum = r.get_text()
			print(b + ',' + recallNum)
	    
	    # Write all the data to the CSV file
	    # csv_writer.writerow([station_lat, station_lon])