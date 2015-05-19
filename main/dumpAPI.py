import urllib3
import urllib
import os
import requests

def bingCall(zipCode, address, code = 'S'):
    address = urllib.quote(address)
    apiCall = "http://dev.virtualearth.net/REST/v1/Routes/Transit?wayPoint.0={}&Waypoint.1={}&timeType=Arrival&dateTime=9:00:00AM&key=AtPEU-wNXR1UeeZxhdUhxvt0K29F11jBnDmuKMEOOCBTGu3yanECQlOTyD20cPnV"
    apiCall = apiCall.format(zipCode, address)
    
    print '---'
    print apiCall
    print '---'
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(apiCall)
    
    if r.status_code == 200:
        writeToFile(zipCode, r.content, code)
    else:
        print "Error in HTTP response", r.status_code, r.content


def writeToFile(zipCode, data, code = 'S'):
    mydir = os.path.dirname(os.path.realpath(__file__))
    mydir += '/output' + code + '/'
    if not os.path.exists(mydir):
        os.makedirs(mydir)
    f = open(mydir + zipCode + '.txt', 'w')
    f.write(data)
    f.close()


if __name__ == '__main__':
    writeToFile('07306', data = 'abc', code = 'S')