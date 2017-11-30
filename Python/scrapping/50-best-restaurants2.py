# Import the BeautifulSoup Library
from bs4 import BeautifulSoup
# Import the URL Library
import urllib
# Import the CSV library to export as a CSV file
# import csv

arrayURLs = ['http://www.theworlds50best.com/The-List-2017/1-10/Eleven-Madison-Park.html','http://www.theworlds50best.com/The-List-2017/1-10/Osteria-Francescana.html','http://www.theworlds50best.com/The-List-2017/1-10/El-Celler-de-Can-Roca.html','http://www.theworlds50best.com/The-List-2017/1-10/Mirazur.html','http://www.theworlds50best.com/The-List-2017/1-10/Central.html','http://www.theworlds50best.com/The-List-2017/1-10/Asador-Etxebarri.html','http://www.theworlds50best.com/The-List-2017/1-10/Gaggan.html','http://www.theworlds50best.com/The-List-2017/1-10/Maido.html','http://www.theworlds50best.com/The-List-2017/1-10/Mugaritz.html','http://www.theworlds50best.com/The-List-2017/1-10/Steirereck.html','http://www.theworlds50best.com/The-List-2017/11-20/Blue-Hill-at-Stone-Barns.html','http://www.theworlds50best.com/The-List-2017/11-20/Arpege.html','http://www.theworlds50best.com/The-List-2017/11-20/Alain-Ducasse-au-Plaza-Athenee.html','http://www.theworlds50best.com/The-List-2017/11-20/Restaurant-Andre.html','http://www.theworlds50best.com/The-List-2017/11-20/Piazza-Duomo.html','http://www.theworlds50best.com/The-List-2017/11-20/DOM.html','http://www.theworlds50best.com/The-List-2017/11-20/Le-Bernardin.html','http://www.theworlds50best.com/The-List-2017/11-20/Narisawa.html','http://www.theworlds50best.com/The-List-2017/11-20/Geranium.html','http://www.theworlds50best.com/The-List-2017/11-20/Pujol.html','http://www.theworlds50best.com/The-List-2017/21-30/Alinea.html','http://www.theworlds50best.com/The-List-2017/21-30/Quintonil.html','http://www.theworlds50best.com/The-List-2017/21-30/White-Rabbit.html','http://www.theworlds50best.com/The-List-2017/21-30/Amber.html','http://www.theworlds50best.com/The-List-2017/21-30/Tickets.html','http://www.theworlds50best.com/The-List-2017/21-30/The-Clove-Club.html','http://www.theworlds50best.com/The-List-2017/21-30/The-Ledbury.html','http://www.theworlds50best.com/The-List-2017/21-30/Nahm.html','http://www.theworlds50best.com/The-List-2017/21-30/Le-Calandre.html','http://www.theworlds50best.com/The-List-2017/21-30/Arzak.html','http://www.theworlds50best.com/The-List-2017/31-40/Pavillon-Ledoyen.html','http://www.theworlds50best.com/The-List-2017/31-40/Attica.html','http://www.theworlds50best.com/The-List-2017/31-40/Astrid-y-Gaston.html','http://www.theworlds50best.com/The-List-2017/31-40/De-Librije.html','http://www.theworlds50best.com/The-List-2017/31-40/Septime.html','http://www.theworlds50best.com/The-List-2017/31-40/Dinner-by-Heston-Blumenthal.html','http://www.theworlds50best.com/The-List-2017/31-40/Saison.html','http://www.theworlds50best.com/The-List-2017/31-40/Azurmendi.html','http://www.theworlds50best.com/The-List-2017/31-40/Relae.html','http://www.theworlds50best.com/The-List-2017/31-40/Cosme.html','http://www.theworlds50best.com/The-List-2017/41-50/Ultraviolet-by-Paul-Pairet.html','http://www.theworlds50best.com/The-List-2017/41-50/Borago.html','http://www.theworlds50best.com/The-List-2017/41-50/Reale.html','http://www.theworlds50best.com/The-List-2017/41-50/Brae.html','http://www.theworlds50best.com/The-List-2017/41-50/Den.html','http://www.theworlds50best.com/The-List-2017/41-50/LAstrance.html','http://www.theworlds50best.com/The-List-2017/41-50/Vendome.html','http://www.theworlds50best.com/The-List-2017/41-50/Restaurant-Tim-Raue.html','http://www.theworlds50best.com/The-List-2017/41-50/Tegui.html','http://www.theworlds50best.com/The-List-2017/41-50/Hof-Van-Cleve.html']

for url in arrayURLs:
	# print url
	# Load in and read the URL
	r = urllib.urlopen(url).read()
	# Pass the HTML from the URL into BeautifulSoup
	soup = BeautifulSoup(r)

	# Loop through all the HTML data and pull out the important information using the specific labels and IDs
	for link in soup.findAll('body'):
		name = link.find('h1').get_text()
		last_ul = link.find('div', attrs={'class', 'c-4 nr nt'}).findAll('ul')[-2].get_text()
		print(last_ul)
	    
	    # Write all the data to the CSV file
	    # csv_writer.writerow([station_lat, station_lon])