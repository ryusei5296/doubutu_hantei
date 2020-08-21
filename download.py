from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# APIキーの情報

key = "6ec87f1d7433abacf13ad04399fe085f"
secret = "097442a7a4137669"
wait_time = 1

#保存フォルダの指定
animalname = sys.argv[1]
savedir = "./" + animalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = animalname,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + './' + photo['id'] + '.jpg'
    if os.path.exists(filepath): # filepathが存在していれば True
        continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
