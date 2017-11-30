import requests

arrayURLs = ['11 Madison Avenue, New York 10010',
'121099, Russia, Moscow, Smolenskaya Square, Building 3, 16th Floor ',
'127 Ledbury Road, Notting Hill, London W11 2AQ',
'155 West 51st St, New York, NY 10019',
'1723 North Halsted, Chicago, Illinois 60614',
'178 Townsend St, San Francisco, CA 94107',
'2-3-18 Jingumae Shibuya-ku, Tokyo',
'25 Avenue Montaigne, 75008 Paris',
'27 South Sathorn Road, Thung Maha Mek, Sathon, Bangkok 10120',
'30 Avenue Aristide Briand, 06500 Menton',
'35 E 21st St, New York, NY 10010',
'380 Old Street, London EC1V 9LT',
'399 San Martin Street, Miraflores, Lima',
'4 Rue Beethoven, 75116, Paris',
'41 Bukit Pasoh Road, Singapore 089855',
'4285 Cape Otway Rd., Birregurra, Victoria ',
'630 Bedford Road, Tarrytown, Pocantico Hills, New York 10591',
'68/1 Soi Langsuan, Ploenchit Road, Lumpini, Bangkok 10330',
'7/F The Landmark Mandarin Oriental, The Landmark, 15 Queens Road, Central, Hong Kong',
'74 Glen Eira Rd, Ripponlea, Victoria, 3185',
'8 Avenue Dutuit, 75008 Paris',
'80 Rue de Charonne, Paris 11',
'84 Rue de Varenne, 75007, Paris',
'Aldura Aldea, 20, 20100 Errenteria, Gipuzkoa',
'Althoff Grandhotel Schloss Bensberg, Kadettenstrasse, 51429 Bergisch Gladbach, Cologne',
'Am Heuemarkt 2A/im Stadtpark, A-1030 Vienna',
'Av Alcalde Elsegui, 273, 20015 San Donostia San Sebastin, Guipzcoa',
'Av. Nueva Costanera 3467, Vitacura, Santiago',
'Av. Paz Soldain 290, San Isidro, Lima 27',
'Avinguda Paralalel 164, Barcelona 08015',
'c/o Bund 18, 6/F, 18 Zhongshan Dong Yi Lu, Shanghai 20000',
'Calle Can Sunyer 48, 17007 Girona ',
'Calle Santa Isabel 376, Miraflores, Lima',
'Corredor del Txorierri Salida 25, Larrabetzu, Bizkaia',
'Costa Rica 5852, C1414BTJ CABA',
'Jagersborggade 41, 2200, Kobenhavn N',
'Mandarin Oriental Hyde Park, 66 Knightsbridge, London SW1X 7LA',
'Minami Ayoyama 2-6-15, Minato-ku, Tokyo, 107-0062',
'Newton 55, Polanco, Mexico City',
'Per Henrik Lings Alla 4, 8. DK-2100 Copenhagen',
'Piana Santa Liberata 67031, Castel di Sangro ',
'Piazza Risorgimento, 4, 12051 Alba',
'Plaza de San Juan 1, 48291 Atxondo, Bizkaia',
'Riemegemstraat 1, 9770 Kruishoutem',
'Rua Baro de Capanema, 549, Jardins, Sao Paulo',
'Rudi-dutschke-str. 26, 10969 Berlin',
'Spinhuisplein 1, 8011 ZZ Zwolle',
'Tennyson 133, Polanco 11550, Mexico City',
'Via Liguria 1, 35030 Sarmeola di Rubano, Padua',
'Via Stella 22, 41121 Modena']

for l in arrayURLs:
	url = 'https://maps.googleapis.com/maps/api/geocode/json'
	params = {'sensor': 'false', 'address': l}
	r = requests.get(url, params=params)
	results = r.json()['results']
	location = results[0]['geometry']['location']
	print(l, location['lat'], location['lng'])





