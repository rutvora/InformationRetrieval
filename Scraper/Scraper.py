import requests
from pprint import pprint

base_url = 'http://api.musixmatch.com/ws/1.1/'
api_key = 'apikey=132089eb79411e38f50d1b460db0d233&'
artist_query = base_url + 'artist.search?' + api_key + 'q_artist=prodigy&page_size=10'
r = requests.get(artist_query)
artist_dict = r.json()
artist_list=artist_dict['message']['body']['artist_list']
artist_ids = list()

for i in range(len(artist_list)):
    artist_ids.append(artist_list[i]['artist']['artist_id'])

albums_query=base_url+'artist.albums.get?'+api_key+'artist_id='+str(artist_ids[0])+'&s_release_date=desc'
r= requests.get(albums_query)
pprint(r.json())
