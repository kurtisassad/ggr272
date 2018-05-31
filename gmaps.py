#AIzaSyBGMliL8iD5VWuDcmq_9xGvsmwz2QbJYn4
#https://maps.googleapis.com/maps/api/distancematrix/json?origins=1026+Forestwood+Drive&destinations=UTM+Mississauga+Road+Mississauga+ON&mode=transit&key=AIzaSyBGMliL8iD5VWuDcmq_9xGvsmwz2QbJYn4
import json
import time
import urllib.request
import urllib.parse
import csv
import time
import random

def _parseResponse(response,retVal):
    for place in response['results']:
        lat = place['geometry']['location']['lat']
        lng = place['geometry']['location']['lng']
        id = place['place_id']
        name = place['name']
        rating = 0
        try:
            rating = place['rating']
        except:
            pass
        loc = place['vicinity']
        if 'Toronto' in loc:
            retVal['restaurants'].append({'lat':lat,'lng':lng,'name':name,'rating':rating,'loc':loc,'id':id})

        pass
def get_data(storage,start,radius,keyword):
    maps_key = 'AIzaSyCVB8ZL09Uq-5ZRDRUmJYJ2CBQEXGLkfGw'
    base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    next_page_token = ''
    while next_page_token != None:
        if next_page_token != '':
            url = base_url + '?' + urllib.parse.urlencode({
                'pagetoken':next_page_token,
                'location': start,
                'radius' : radius,
                'rankBy':'distance',
                'keyword':keyword,
                'key': maps_key,
            }, safe='|')
        else:
            url = base_url + '?' + urllib.parse.urlencode({
                'location': start,
                'radius' : radius,
                'rankBy':'distance',
                'keyword':keyword,
                'key': maps_key,
            }, safe='|')
        response = str(urllib.request.urlopen(url).read().decode('UTF-8'))
        result = json.loads(response.replace('\\n', ''))
        try:
            next_page_token = result['next_page_token']
        except:
            next_page_token = None
        print(url)
        print(json.dumps(result, indent=4, sort_keys=True))
        _parseResponse(result,storage)
        time.sleep(2)
def get_multiple(data,start,radius):
    storage = {'restaurants':[]}
    for keyword in data:
        get_data(storage,start,radius,keyword)
    return storage

if __name__ == "__main__":
    storage = {'restaurants':[]}
    names = ["Wendy's","Burger King","A&W Canada","KFC","McDonald's","Subway"]
    for name in names:
        get_data(storage,'43.6629,-79.3957','15000',name)
    # print(storage)
    print(len(storage['restaurants']))
    with open('fourthtry.txt', 'w') as outfile:
        json.dump(storage, outfile)
