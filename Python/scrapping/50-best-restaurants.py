# Import the BeautifulSoup Library
from bs4 import BeautifulSoup
# Import the URL Library
import urllib
# Import the CSV library to export as a CSV file
import csv

count = 0

# Load in and read the URL
r = urllib.urlopen('http://www.theworlds50best.com/list/1-50-winners').read()
# Pass the HTML from the URL into BeautifulSoup
soup = BeautifulSoup(r)

# Write the CSV file (pass in a file name and the 'w' stands for write)
# with open('Desktop/50-best-restaurnats.csv', 'w') as csvfile:
# 	csv_writer = csv.writer(csvfile)

#     # Write headers to the CSV file
# 	csv_writer.writerow(['Link'])

# Loop through all the HTML data and pull out the important information using the specific labels and IDs
for a in soup.findAll('div', attrs={'class': 'c-4'}):
	link = a.find('a')['href']
	print(link)
		# print(b.find('ul')[-1])
	    # print(this_week + "," + last_week_edited + "," + song_title + "," + artist_title)
	    
	    # Write all the data to the CSV file
	    # csv_writer.writerow([this_link])