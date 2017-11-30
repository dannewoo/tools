import requests
import csv

# "Droysigg",

arrayURLs = ["Grundy,VA","Chardon,OH","Alor Akar","Chiang Rai Province","Moses Lake,WA","Freising","San Diego,CA","Tucson,AZ","Hazard,KY","Guatemala City","Jiudian","Erlangen","Brampton,ON","Santee,CA","Los Angeles,CA","Waikino","San Diego,CA","Greenwood,SC","Ottawa,ON","Columbia,SC","Costa Mesa,CA","Melbourne,Victoria","Xichang","Great Barrington,MA","Amphoe Pak Phanang","Maoming","Leizhou,Guangdong","Mazhan","Raumanmeri secondary school,Rauma"]

with open('school-shootings2.csv', 'w') as csvfile:
	csv_writer = csv.writer(csvfile)
	csv_writer.writerow(['Name', 'Lat', 'Lon'])

	for l in arrayURLs:
		url = 'https://maps.googleapis.com/maps/api/geocode/json'
		params = {'sensor': 'false', 'address': l}
		r = requests.get(url, params=params)
		results = r.json()['results']
		location = results[0]['geometry']['location']
		# print(l, location['lat'], location['lng'])

		csv_writer.writerow([l, location['lat'], location['lng']])
