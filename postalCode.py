import json
import time
import urllib.request
import urllib.parse
import csv
import time
import random
def get_postal_code(id):
    maps_key = 'AIzaSyD1C4-WW5TdeASTh1vfNic6KFgBQ3uyZnQ'
    base_url = 'https://maps.googleapis.com/maps/api/place/details/json'
    next_page_token = ''
    url = base_url + '?' + urllib.parse.urlencode({
        'placeid': id,
        'key': maps_key,
    }, safe='|')
    response = str(urllib.request.urlopen(url).read().decode('UTF-8'))
    result = json.loads(response.replace('\\n', ''))
    print(json.dumps(result, indent=4, sort_keys=True))
    formatted = result['result']['formatted_address']
    try:
        num = result['result']['formatted_phone_number']
    except:
        num = None
    return [formatted,num]
def add_postal_code(data):
    for restaurants in data['restaurants']:
        retVal = get_postal_code(restaurants['id'])
        restaurants['formatted'] = retVal[0]
        restaurants['phone'] = retVal[1]

if __name__ == '__main__':
    with open('fourthtry.txt','r') as fp:
        data = json.load(fp)
    for restaurants in data['restaurants']:
        retVal = get_postal_code(restaurants['id'])
        restaurants['formatted'] = retVal[0]
        restaurants['phone'] = retVal[1]
    with open('fourthtryformatted.txt', 'w') as outfile:
        json.dump(data, outfile)
