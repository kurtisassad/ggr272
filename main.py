from gmaps import get_multiple
from postalCode import add_postal_code
from nearGym import add_near_place
import json

def main(keywords,start,radius):
    data = get_multiple(keywords,start,radius)
    add_postal_code(data)
    add_near_place(data,radius_near_key_point,near_key_point)
    with open('data2.json', 'w') as outfile:
        json.dump(data,outfile)

if __name__ == '__main__':
    keywords = ["Wendy's","Burger King","A&W Canada","Quik Chik","KFC",
             "Harvey's","McDonald's","Subway","Popeyes"]
    start = '43.6629,-79.3957' #uoft coordinates
    radius = '15000' #in meters
    near_key_point='gym'
    radius_near_key_point='1000'
    main(keywords,start,radius,near_key_point,radius_near_key_point)
