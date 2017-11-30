import requests

arrayURLs = ["Mundfordville, Kentucky","Murfreesboro, Tennessee","Murray, Kentucky","Muscogee, Georgia","Nancy, Kentucky","Nashville, Tennessee","Natchez, Mississippi","Natural Bridge Station, Virginia","Neosho, Missouri","New Albany, Mississippi","New Castle, Virginia","New Edinburg, Arkansas","New Kent, Virginia","New Market, Virginia","New Orleans, Louisiana","Newberry, South Carolina","Newnan, Georgia","Newport News, Virginia","Newport, Tennessee","Newton, North Carolina","Nicholasville, Kentucky","Nickelsville, Virginia","Norfolk, Virginia","North, South Carolina","Nottoway, Virginia","Oak Hill, Tennessee","Ocala, Florida","Ocilla, Georgia","Odessa, Texas","Oklahoma City, Oklahoma","Okolona, Mississippi","Old Pleasant Hill, Louisiana","Opelika, Alabama","Opelousas, Louisiana","Orangeburg, South Carolina","Orlando, Florida","Osceola, Arkansas","Owensboro, Kentucky","Oxford, Mississippi","Oxford, North Carolina","Ozark, Alabama","Paducah, Kentucky","Palatka, Florida","Palestine, Texas","Palmyra, Missouri","Palmyra, Virginia","Pampa, Texas","Paris, Tennessee","Paris, Texas","Parkers Crossroads, Tennessee","Parkersburg, West Virginia","Parksley, Virginia","Pascagoula, Mississippi","Pauls Valley, Oklahoma","Pea Ridge, Arkansas","Pearisburg, Virginia","Pecos, Texas","Pensacola, Florida","Perry, Florida","Perry, Georgia","Perryton, Texas","Perryville, Kentucky","Petersburg, Virginia","Petersburg/Suffolk, Virginia","Philadelphia, Mississippi","Phoenix, Arizona","Picacho Pass, Arizona","Picayune, Mississippi","Pine Bluff, Arkansas","Pineville, Louisiana","Pittsboro, North Carolina","Plaquemine, Louisiana","Pontotoc, Mississippi","Port Allen, Louisiana","Port Arthur, Texas","Port Gibson, Mississippi","Port Orange, Florida","Portsmouth, Virginia","Potomac, Maryland","Powhatan, Virginia","Prairie, Mississippi","Prattville, Alabama","Prentiss, Mississippi","Prescott, Arkansas","Princeton, Kentucky","Prosperity, South Carolina","Pulaski, Tennessee","Pulaski, Virginia","Purcellville, Virginia","Quicksburg, Virginia","Quincy, Florida","Quitman, Georgia","Quitman, Mississippi","Raeford, North Carolina","Raleigh, North Carolina","Rankin, Texas","Raymond, Mississippi","Rayne, Louisiana","Raywick, Kentucky","Reams, Virginia","Rentiesville, Oklahoma","Rhoadesville, Virginia","Richmond, Texas","Richmond, Virginia","Ridgley, Tennessee","Ridgley, Texas","Ringgold, Georgia","Ripley, Mississippi","Ripley, Tennessee","Roanoke, Missouri","Roanoke, Virginia","Robert Lee, Texas","Rock Hill, South Carolina","Rockingham, North Carolina","Rockville, Maryland","Rocky Mount, North Carolina","Rocky Mount, Virginia","Rogersville, Alabama","Roma, Texas","Roxboro, North Carolina","Rusk, Texas","Russellville, Arkansas","Russellville, Kentucky","Rutherfordton, North Carolina","Salem, South Carolina","Salisbury, North Carolina","Saluda, South Carolina","San Angelo, Texas","San Antonio, Texas","San Diego, California","Sanderson, Texas","Sandston, Virginia","Sanford, North Carolina","Sappington, Missouri","Sardis, Tennessee","Satsuma, Alabama","Savannah, Georgia","Savannah, Tennessee","Searcy, Arkansas","Selma, Alabama","Selma, North Carolina","Selmer, Tennessee","Senatobia, Mississippi","Sewanee, Tennessee","Sharpsburg, Georgia","Shelby, North Carolina","Sherman, Texas","Shreveport, Louisiana","Smithville, Arkansas","Smithville, Tennessee","Smyrna, Tennessee","Snake Range Mountains, Nevada","Snow Hill, North Carolina","Snyder, Texas","Somerset, Kentucky","Sonora, Texas","Southampton County, Virginia","Sparta, Georgia","Spartanburg, South Carolina","Spencer, North Carolina","Spencer, Tennessee","Spotsylvania, Virginia","Spring Lake, North Carolina","Springdale, Arkansas","Springfield, Georgia","Springfield, Tennessee","Springfield, Virginia","St. Augustine, Florida","St. Cloud, Florida","St. Francisville, Louisiana","St. Joseph, Kentucky","St. Louis, Missouri","St. Matthews, South Carolina","Star City, Arkansas","Starke, Florida","Statesboro, Georgia","Staunton, Virginia","Stephenson, Virginia","Sterling City, Texas","Stone Mountain, Georgia","Stonewall, Louisiana","Stonewall, Mississippi","Stonewall, North Carolina","Stonewall, Oklahoma","Stonewall, Texas","Stuart, Florida","Stuart, Virginia","Summerville, South Carolina","Sumner, Mississippi","Surry, Virginia","Sussex, Virginia","Sweetwater, Texas","Sylva, North Carolina","Tahlequah, Oklahoma","Tallahassee, Florida","Tallulah, Louisiana","Tampa, Florida","Tappahannock, Virginia","Tarboro, North Carolina","Taylorsville, North Carolina","Tazewell, Virginia","Terre Haute, Indiana","Texarkana, Texas","Thibodaux, Louisiana","Thomaston, Georgia","Thomasville, North Carolina","Thomson, Georgia","Tifton, Georgia","Timmonsville, South Carolina","Toccoa, Georgia","Tomball, Texas","Trenton, Georgia","Trenton, North Carolina","Trenton, South Carolina","Trenton, Tennessee","Troy, Alabama","Trussville, Alabama","Tullahoma, Tennessee","Tulsa, Oklahoma","Tupelo, Mississippi","Tuscaloosa, Alabama","Tuscumbia, Alabama","Tuskegee, Alabama","Tyler, Texas","Union City, Tennessee","Union Point, Georgia","Union Springs, Alabama","Union, South Carolina","Union, West Virginia","University, Mississippi","Vaiden, Mississippi","Van Buren, Arkansas","Vega, Texas","Vernon, Texas","Verona, Virginia","Versailles, Kentucky","Victoria, Texas","Vienna, Georgia","Virginia Beach, Virginia","Wadesboro, North Carolina","Wagener, South Carolina","Walhalla, South Carolina","Walterboro, South Carolina","Warm Springs, Virginia","Warner Robins, Georgia","Warrenton, Georgia","Warrenton, North Carolina","Washington, D.C.","Washington, Georgia","Washington, Virginia","Water Valley, Kentucky","Watha, North Carolina","Waveland, Mississippi","Waverly, Missouri","Waycross, Georgia","Waynesboro, Tennessee","Waynesboro, Virginia","Waynesville, North Carolina","Weatherford, Texas","Weldon, North Carolina","Wesson, Mississippi","West Alton, Missouri","West Point, Mississippi","Westminster, South Carolina","Weston, West Virginia","Wheeler, Alabama","White Springs, Florida","Wichita, Kansas","Wilkes-Barre, Pennsylvania","Wilkesboro, North Carolina","Williamsburg, Virginia","Williamston, South Carolina","Wilmington, North Carolina","Wilson, Arkansas","Wilson, North Carolina","Winchester, Virginia","Windsor, North Carolina","Windsor, Virginia","Winnfield, Louisiana","Winnsboro, South Carolina","Winona, Mississippi","Winston-Salem, North Carolina","Winton, North Carolina","Wise, Virginia","Woodford, Virginia","Wrightsville, Georgia","Yanceyville, North Carolina","Yazoo City, Mississippi","York, South Carolina","Zachary, Louisiana","Zephyrhills, Florida"]

for l in arrayURLs:
	url = 'https://maps.googleapis.com/maps/api/geocode/json'
	params = {'sensor': 'false', 'address': l}
	r = requests.get(url, params=params)
	results = r.json()['results']
	location = results[0]['geometry']['location']
	print(l, location['lat'], location['lng'])




