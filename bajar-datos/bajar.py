from flickrapi import FlickrAPI
import keys

flickr = FlickrAPI(keys.API_KEY, keys.API_SECRET, format='parsed-json')
