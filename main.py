import requests
import urllib
from bs4 import BeautifulSoup
import json
from collections import OrderedDict
from datetime import datetime

hdr = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.melon.com/chart/index.htm'

res = requests.get(url, headers=hdr)

text = res.text

soup = BeautifulSoup(text, 'html.parser')

count = 1
file_data = OrderedDict()
file_data['date'] = str(datetime.today().date())
file_data['chart'] = []
for tr in soup.select('#frm > div > table > tbody > tr'):
    thing = OrderedDict()
    song = tr.select_one('div.ellipsis').a.text.strip()
    name = tr.select_one('span.checkEllipsis').a.text.strip()
    album = tr.select_one('div.rank03').a.text.strip()
    # like = tr.select_one('span.cnt').text.strip()
    # img = tr.select_one('a.image_typeAll').img.get('src')
    #
    # idx = img.split('/melon/')
    # urllib.request.urlretrieve(idx[0], './img/' + album.replace("/", ""))

    thing['rank'] = str(count)
    thing['name'] = song
    thing['singer'] = name
    thing['album'] = album

    file_data['chart'].append(thing)
    # print(str(count) + "위", song, name, album)
    count += 1

print(json.dumps(file_data, ensure_ascii=False, indent='\t'))
with open(file_data['date'] + '.json', 'w', encoding='utf-8') as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent='\t')