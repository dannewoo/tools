import requests
import csv

# "Droysigg",

arrayURLs = ["Berkeley, California","Santa Cruz, California","Minneapolis, Minnesota","Seattle, Washington","Grand Rapids, Minnesota","Minnesota State University, Mankato","St. Paul, Minnesota","Albuquerque, New Mexico","Portland, Oregon","Traverse City, Michigan","Akron/Newstead, New York","Olympia, Washington","Village of Lewiston, New York","Anadarko, Oklahoma","Carrboro, North Carolina","Belfast, Maine","San Fernando, California","Alpena, Michigan","Bexar County, Texas","Denver, Colorado","State of Minnesota","State of Vermont","University of Utah","Brown University","Cornell University","Syracuse University","Ann Arbor, Michigan","Spokane, Washington","Bainbridge Island, Washington","East Lansing, Michigan","Santa Fe, New Mexico","Phoenix, Arizona","State of Alaska","Ypsilanti, Michigan","Durango, Colorado","Asheville, North Carolina","Eugene, Oregon","Cambridge, Massachusetts","Boulder, Colorado","Harpers Ferry, West Virginia","Lawrence, Kansas","Amherst, Massachusetts","Northampton, Massachusetts","Austin, Texas","Bangor, Maine","Brunswick, Maine","Burbank, California","Davenport, Iowa","Durham, New Hampshire","Iowa City, Iowa","Ithaca, New York","Johnson County, Iowa","Long Beach, California","Los Angeles, California","Los Angeles County, California ","Moscow, Idaho","Norman, Oklahoma","Oberlin, Ohio","Orono, Maine","Portland, Maine","Salt Lake City, Utah","San Luis Obispo, California","Tulsa, Oklahoma ","Tahlequah, Oklahoma ","Watsonville, California","Nashville, Tennessee"]

with open('indigenous-people-day.csv', 'w') as csvfile:
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
