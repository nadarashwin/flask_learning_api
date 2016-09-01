#!/usr/local/bin/python2.7

import requests
import json
import key

import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stdout)

__user = raw_input("please enter the address to be:- ")
__meal = raw_input("meal type please:- ")

def getGeoCodeLocation(inputstring):
	locationstring = inputstring.replace(" ", "+")
	url = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" %(locationstring, key.google_api_key))
	data = json.loads(url.text)
	lat = data['results'][0]['geometry']['location']['lat']
	lng = data['results'][0]['geometry']['location']['lng']
	#print "response header: %s \n \n" % url.response
	return (lat, lng)

def foursquare(inputstring):
	lt, lg = getGeoCodeLocation(__user)
	url = requests.get("https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20160901&ll=%f,%f&query=%s" %(key.foursquare_cli_key,key.foursquare_cli_sec,lt,lg,inputstring))
	data = json.loads(url.text)
	for i in range(0,len(data['response']['venues'])):
		__id = data['response']['venues'][i]['id']
		url_photo = requests.get("https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&client_secret=%s&v=20160901" %(__id,key.foursquare_cli_key,key.foursquare_cli_sec))
		photo = json.loads(url_photo.text)
		print "Name of the Store:- " + str(data['response']['venues'][i]['name'])
		try:
			print "Address of the Store:- " + str(data['response']['venues'][i]['location']['address'])
		except:
			print "No Address found though id is:- " + str(data['response']['venues'][i]['id'])
		try:
			print "an image to go through is :- " + photo['response']['photos']['items'][i]['prefix'] + "300x300" + photo['response']['photos']['items'][i]['suffix']
		except:
			print "No Image found though id is:- " + str(data['response']['venues'][i]['id'])

foursquare(__meal)
