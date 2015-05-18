
class CityTaxRates():
    
    def __init__(self):
        self.map = {}
    
    def load(self, filename):
        with open(filename) as f:
            st = f.readline()
            st = st.trim();
            if len(st) != 0:
                arr = st.split(' ')
                rate = float(arr[0])
                city_name = arr[0:-2]
                self.map[city_name] = rate
    
    def getCityTaxRate(self, city):
        return self.map[city]


def get_city_from_zipcode(zipcode):
    pass; 


    