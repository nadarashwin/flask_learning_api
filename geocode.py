#!/usr/local/bin/python2.7

import requests
import json


import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stdout)

__user = raw_input("please enter the address to be:- ")
__meal = raw_input("meal type please:- ")

def getGeoCodeLocation(inputstring):
	google_api_key = ""
	locationstring = inputstring.replace(" ", "+")
	url = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" %(locationstring, google_api_key))
	data = json.loads(url.text)
	lat = data['results'][0]['geometry']['location']['lat']
	lng = data['results'][0]['geometry']['location']['lng']
	#print "response header: %s \n \n" % url.response
	return (lat, lng)

def foursquare(inputstring):
	lt, lg = getGeoCodeLocation(__user)
	foursquare_client_key = ""
	foursquare_client_sec = ""
	url = requests.get("https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20160901&ll=%f,%f&query=%s" %(foursquare_client_key,foursquare_client_sec,lt,lg,inputstring))
	print json.loads(url.text)
foursquare(__meal)