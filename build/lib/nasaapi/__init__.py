from json import loads as load
from random import randint as random
import requests

__version__ = '0.0.2'

class MarsRovers():

    def __init__(self, api_key, sols=random(0, 2000), camera="fhaz"):
        self.api_key = api_key
        self.sols = str(sols)
        self.camera = str(camera)

    def curiosity(self):
        return load(requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=' + self.sols + '&camera=' + self.camera + '&api_key=' + self.api_key).text)
        
    def spirit(self):
        return load(requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos?sol=' + self.sols + '&camera=' + self.camera + '&api_key=' + self.api_key).text)

    def opportunity(self):
        return load(requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?sol=' + self.sols + '&camera=' + self.camera + '&api_key=' + self.api_key).text)

class NIVL():

    def __init__(self, api_key):
        self.api_key = api_key
        self.base = 'https://images-api.nasa.gov/'

    def search(self, query):
        return load(requests.get(self.base + 'search?q=' + query).text)

    def asset(self, id):
        return load(requests.get(self.base + 'asset/' + id).text)
    
    def metadata(self, id):
        return load(requests.get(self.base + 'metadata/' + id).text)
    
    def captions(self, id):
        return load(requests.get(self.base + 'captions/' + id).text)

class TLE():

    def search(self, query):
        return load(requests.get('https://data.ivanstanojevic.me/api/tle?search=' + query).text)
    
    def get(self, query):
        return load(requests.get('http://data.ivanstanojevic.me/api/tle/' + query).text)

class Client():

    def __init__(self, api_key):
        self.api_key = api_key
        self.tle = TLE()
        self.nivl = NIVL(self.api_key)

    def apod(self):
        return load(requests.get('https://api.nasa.gov/planetary/apod?api_key=' + self.api_key).text)

    def apod_image(self):
        return load(requests.get('https://api.nasa.gov/planetary/apod?api_key=' + self.api_key).text).url

    def earth(self, lat, lon, date):
        return load(requests.get('https://api.nasa.gov/planetary/earth/assets?lon=' + str(lon) + '&lat=' + str(lat) + '&date=' + str(date) + '&&dim=0.10&api_key=' + self.api_key).text)

    def earth_image(self, lat, lon, date):
        try:
            load(requests.get('https://api.nasa.gov/planetary/earth/assets?lon=' + str(lon) + '&lat=' + str(lat) + '&date=' + str(date) + '&&dim=0.10&api_key=' + self.api_key).text).url
        except:
            return None

    def insight(self):
        return load(requests.get('https://api.nasa.gov/insight_weather/?api_key=' + self.api_key + '&feedtype=json&ver=1.0').text)

    def mars_rovers(self, sols=random(0, 2000), camera="fhaz"):
        return MarsRovers(self.api_key, sols, camera)

    def techport(self, id):
        try:
            return load(requests.get('https://api.nasa.gov/techport/api/projects/' + id + '?api_key=' + self.api_key).text)
        except:
            return 'invalid id'