import urllib2
import os

# def bingCall(zipCode, address, code = 'S'):
#     address = urllib.quote(address)
#     apiCall = "http://dev.virtualearth.net/REST/v1/Routes/Transit?wayPoint.0={}&Waypoint.1={}&timeType=Arrival&dateTime=9:00:00AM&key=AtPEU-wNXR1UeeZxhdUhxvt0K29F11jBnDmuKMEOOCBTGu3yanECQlOTyD20cPnV"
#     apiCall = apiCall.format(zipCode, address)
#     
#     print '---'
#     print apiCall
#     print '---'
#     
#     r = requests.get(apiCall)
#     
#     if r.status_code == 200:
#         writeToFile(zipCode, r.content, code)
#     else:
#         print "Error in HTTP response", r.status_code, r.content


def googleCall(zipCode, address, code = 'S'):
    address = urllib2.quote(address)
    apiCall = "https://maps.googleapis.com/maps/api/directions/json?origin={}&destination={}&mode=transit&arrival_time=1432126800&key=AIzaSyBmtTHg-FrchEae3TgjH04BX0mpAKBuN-Y"
    apiCall = apiCall.format(zipCode, address)
    
    print '---'
    print apiCall
    print '---'

    try:
        req = urllib2.Request(apiCall)
        response = urllib2.urlopen(req)
        data = response.read()
        writeToFile(zipCode, data, code)
    except urllib2.URLError, e:
        print e.reason
        

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