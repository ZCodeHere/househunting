from util import initZipCode, initCityTaxRate
import dumpAPI
import time
from random import randint

def main():
    zipCodeGist = initZipCode(['hudson', 'bergen', 'essex', 'middlesex', 'morris', 
                               'passaic', 'somerset', 'sussex', 'union'])
    cityTaxRate = initCityTaxRate()
    
    print zipCodeGist.getAllZipCodes()
    print len(zipCodeGist.getAllZipCodes())
    
    for zipcode in zipCodeGist.getAllZipCodes():
        dumpAPI.googleCall(zipcode, '250 W 55th St, New York, NY', code = 'S')
        wait = 20 + randint(0,20)
        print "dumped ", zipcode, "waiting for ", wait
        time.sleep(wait)
        
        

if __name__ == '__main__':
    main()