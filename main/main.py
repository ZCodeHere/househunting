from util import initZipCode, initCityTaxRate
import dumpAPI
import time
from random import randint

def main():
    zipCodeGist = initZipCode()
    cityTaxRate = initCityTaxRate()
    
    for zipcode in zipCodeGist.getAllZipCodes():
    #for zipcode in ['07302', '07306']:
        dumpAPI.bingCall(zipcode, '250 W 55th St, New York, NY', code = 'S')
        wait = 60 + randint(0,20)
        print "dumped ", zipcode, "waiting for ", wait
        time.sleep(wait)
        
        

if __name__ == '__main__':
    main()