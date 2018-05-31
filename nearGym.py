#AIzaSyBGMliL8iD5VWuDcmq_9xGvsmwz2QbJYn4
#https://maps.googleapis.com/maps/api/distancematrix/json?origins=1026+Forestwood+Drive&destinations=UTM+Mississauga+Road+Mississauga+ON&mode=transit&key=AIzaSyBGMliL8iD5VWuDcmq_9xGvsmwz2QbJYn4
import json
import time
import urllib.request
import urllib.parse
import csv
import time
import random

def near_gym(start,radius,keyword):
    maps_key = 'AIzaSyD1C4-WW5TdeASTh1vfNic6KFgBQ3uyZnQ'
    base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    url = base_url + '?' + urllib.parse.urlencode({
        'location': start,
        'radius' : radius,
        'rankBy':'distance',
        'keyword':keyword,
        'key': maps_key,
    }, safe='|')
    response = str(urllib.request.urlopen(url).read().decode('UTF-8'))
    result = json.loads(response.replace('\\n', ''))
    print(json.dumps(result, indent=4, sort_keys=True))
    return result['results']!=[]

def add_near_place(data,radius,place):
    for place in data['restaurants']:
        loc = str(place['lat']) + ',' + str(place['lng'])
        place['near_gym'] = near_gym(loc,radius,place)


if __name__ == "__main__":
    with open('fourthtryformatted.txt','r') as fp:
        data = json.load(fp)
    for place in data['restaurants']:
        loc = str(place['lat']) + ',' + str(place['lng'])
        place['near_gym'] = near_gym(loc,'1000','gym')
    with open('fourthtry2.txt', 'w') as outfile:
        json.dump(data,outfile)
