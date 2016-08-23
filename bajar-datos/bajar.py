from flickrapi import FlickrAPI
import json
import sys
import time
import keys

# Parameters definition:
# https://www.flickr.com/services/api/flickr.photos.search.html

# Constants
BOGOTA_FLICKR_ID = '368148' # ID of Bogota in Flickr places database
ACCURACY = 11 # Accuracy to city level
CONTENT_TYPE = 6 # Exclude screenshots from download
PER_PAGE = 250 # Number of results per page (max 250)

# EXTRAS = 'description,license,date_upload,date_taken,owner_name,\
# icon_server,original_format,last_update,geo,tags,machine_tags,\
# o_dims,views,media,path_alias,url_s'

EXTRAS = 'description,date_taken,owner_name,geo,tags,media,path_alias,url_s'

NB_PAGES = 500

##############################################################################

def eprint(*args, **kwargs):
    '''Print in stderr'''
    print(*args, file=sys.stderr, **kwargs)

    
flickr = FlickrAPI(keys.API_KEY, keys.API_SECRET, format='json')

results = []

for curpage in range(1, NB_PAGES+1):
    eprint(curpage)
    page = flickr.photos.search(extras=EXTRAS,
                                 place_id=BOGOTA_FLICKR_ID,
                                 accuracy=ACCURACY,
                                 content_type=CONTENT_TYPE,
                                 per_page=PER_PAGE,
                                 page=curpage)
    results.append(page.decode('utf-8'))
    time.sleep(1) # Tempo to avoid API restriction

results_merged = []
for res in results:
    results_merged.append(json.loads(res))

output = json.dumps(results_merged)

print(output)
