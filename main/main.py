import os
from util import ZipCode


def main():
    initZipCode()

def initZipCode():
    dir = os.path.dirname(os.path.realpath(__file__))
    zipCodeFile = dir + '\..\data\NJ_zipcode.txt'
    
    zipCodeList = []
    
    with open(zipCodeFile) as f:
        while True:
            line = f.readline()
            line = line.trim()
            if (len(line) == 0):
                break
            
            arr = line.split('\t')
            zipcode = arr[1]
            town = arr[2]
            longtitude = float(arr[-2])
            latitude = float(arr[-1])
            zipCodeObj = ZipCode(zipcode, town, longtitude, latitude)
            
            zipCodeList.append(zipCodeObj)

    return zipCodeList

if __name__ == '__main__':
    main()