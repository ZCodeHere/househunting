import os 
import math
 
class CityTaxRates():
    
    def __init__(self):
        self.map = {}
        self.city_list = set()
    
    def load(self, filename):
        with open(filename) as f:
            while True:
                st = f.readline()
                st = st.strip()
                if len(st) == 0:
                    break
                arr = st.split(' ')
                rate = float(arr[-1])
                city_name = ' '.join(arr[0:-2])
                city_name = city_name.lower()
                self.map[city_name] = rate
                self.city_list.add(city_name)
    
    def getCityTaxRate(self, city, approximateName = True):
        city = city.lower()
        bestMatch = self.getBestMatchName(city)
        return self.map[bestMatch]
    
    def getBestMatchName(self, name):
        name = name.lower()
        bestScore = 0
        bestMatch = None
        for city in self.city_list:
            score = self.matchScore(city, name)
            if score > bestScore:
                bestScore = score
                bestMatch = city
        return bestMatch
             
    def matchScore(self, name1, name2):
        ans = 0
        for i in xrange(min(len(name1), len(name2))):
            if (name1[i] == name2[i]):
                ans = i
            else:
                break
        
        ans += ans * 1.0 / max(len(name1), len(name2))
        
        return ans
    
    
class ZipCode():
    def __init__(self, zipCode, cityName, latitude, longitude):
        self.longitude = longitude
        self.latitude = latitude
        self.cityName = cityName
        self.zipCode = zipCode
        

class ZipCodeCollection():
    def __init__(self):
        self.map = {}
        
    def getAllZipCodes(self):
        return self.map.keys()
    
    def addZipCode(self, zz):
        self.map[zz.zipCode] = zz
        
    def distance(self, z1, z2):
        z1 = self.map[z1]
        z2 = self.map[z2]
        return self.distanceZipCodeObj(z1, z2)
    
    def distanceZipCodeObj(self, z1, z2):
        lat1 = z1.latitude
        long1 = z1.longitude
        lat2 = z2.latitude
        long2 = z2.longitude
        
        return distanceByLatLong((lat1, long1), (lat2, long2))
        

def initZipCode():
    dir = os.path.dirname(os.path.realpath(__file__))
    zipCodeFile = dir + '/../data/NJ_zipcode.txt'
    
    zipCodeGist = ZipCodeCollection();
    
    with open(zipCodeFile) as f:
        while True:
            line = f.readline()
            line = line.strip()
            if (len(line) == 0):
                break
            
            arr = line.split('\t')
            zipcode = arr[1]
            town = arr[2]
            town = town.lower()
            latitude = float(arr[-2])
            longitude = float(arr[-1])
            zipCodeObj = ZipCode(zipcode, town, latitude, longitude)
            
            zipCodeGist.addZipCode(zipCodeObj)
            
    return zipCodeGist



def initCityTaxRate():
    taxdir = os.path.dirname(os.path.realpath(__file__))
    taxdir += "/../data/"
    
    counties = ['bergen', 'essex', 'hudson', 'middlesex', 'morris', 'passaic', 'somerset', 'sussex', 'union']
    cityTaxRate = CityTaxRates()
    
    for county in counties:
        filename = taxdir + county + '_tax.txt'
        print filename
        cityTaxRate.load(filename)
    
    return cityTaxRate


def distanceByLatLong(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 3961 # km
 
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
 
    return d 
