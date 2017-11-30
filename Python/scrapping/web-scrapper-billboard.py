# Import the BeautifulSoup Library
from bs4 import BeautifulSoup
# Import the URL Library
import urllib
# Import the CSV library to export as a CSV file
import csv

# Load in and read the URL
r = urllib.urlopen('http://www.billboard.com/charts/hot-100').read()
# Pass the HTML from the URL into BeautifulSoup
soup = BeautifulSoup(r, "html.parser")

# Write the CSV file (pass in a file name and the 'w' stands for write)
with open('Desktop/billboard_top100.csv', 'w') as csvfile:
	csv_writer = csv.writer(csvfile)

    # Write headers to the CSV file
	csv_writer.writerow(['Rank This Week', 'Song', 'Artist', 'Rank Last Week', 'Top Spot', 'Total Number of Weeks'])

	# Loop through all the HTML data and pull out the important information using the specific labels and IDs
	for link in soup.findAll('article', attrs={'class': 'chart-row'}):
	    this_week = link.find('span', attrs={'class': 'chart-row__current-week'}).get_text()
	    last_week = link.find('span', attrs={'class': 'chart-row__last-week'}).get_text().replace('Last Week: ', '')
	    top_spot = link.find('div', attrs={'class': 'chart-row__top-spot'}).find('span', attrs={'class': 'chart-row__value'}).get_text()
	    weeks_on = link.find('div', attrs={'class': 'chart-row__weeks-on-chart'}).find('span', attrs={'class': 'chart-row__value'}).get_text()
	    song_title = link.find('div', attrs={'class': 'chart-row__title'}).find('h2').get_text()
	    artist_title = link.find('div', attrs={'class': 'chart-row__title'}).find(attrs={'class': 'chart-row__artist'}).get_text()
	    # print(this_week + "," + last_week_edited + "," + song_title + "," + artist_title)
	    
	    # Write all the data to the CSV file
	    csv_writer.writerow([this_week, song_title, artist_title[1:], last_week, top_spot, weeks_on])