from flickrapi import FlickrAPI
import keys

# Parameters definition:
# https://www.flickr.com/services/api/flickr.photos.search.html

# Constants
BOGOTA_FLICKR_ID = '368148' # ID of Bogota in Flickr places database
ACCURACY = 11 # Accuracy to city level
CONTENT_TYPE = 6 # Exclude screenshots from download
PER_PAGE = 500 # Number of results per page (max 500)

EXTRAS = 'description,license,date_upload,date_taken,owner_name,\
icon_server,original_format,last_update,geo,tags,machine_tags,\
o_dims,views,media,path_alias,url_s'


##############################################################################

flickr = FlickrAPI(keys.API_KEY, keys.API_SECRET, format='parsed-json')

for curpage in range(1):
    bogota = flickr.photos.search(extras=EXTRAS,
                                 place_id=BOGOTA_FLICKR_ID,
                                 accuracy=ACCURACY,
                                 content_type=CONTENT_TYPE,
                                 per_page=PER_PAGE,
                                 page=curpage)
    photos = bogota['photos']

    print(photos)
