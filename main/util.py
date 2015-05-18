
class CityTaxRates():
    
    def __init__(self):
        self.map = {}
        self.city_list = set()
    
    def load(self, filename):
        with open(filename) as f:
            st = f.readline()
            st = st.trim()
            if len(st) != 0:
                arr = st.split(' ')
                rate = float(arr[0])
                city_name = arr[0:-2]
                self.map[city_name] = rate
                self.city_list.add(city_name)
    
    def getCityTaxRate(self, city, approximateName = True):
        bestMatch = self.getBestMatchName(city)
        return self.map[bestMatch]
    
    def getBestMatchName(self, name):
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
        return ans
    
    
class ZipCode():
    def __init__(self, zipCode, cityName, longtitude, latitude):
        self.longtitude = longtitude
        self.latitude = latitude
        self.cityName = cityName
        self.zipCode = zipCode
        


    