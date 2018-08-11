from os import listdir
from os.path import isfile, join

# init
file = "/Users/Mo/Library/Mobile Documents/com~apple~CloudDocs/Projekte/KML eradicator/bookmarks.kml"
dataArray = []


ifile = open(file, "rU")
KMLtextContents = ifile.read()
ifile.close()


i = 0
indexTemp1 = 0
indexStart = []
indexEnd = []
coordinateData = []

for indexChar in range(0, len(KMLtextContents)):
    if (KMLtextContents[indexChar:indexChar+11] == '<Placemark>'):
        # Start found now look for end
        indexStart.append(indexChar)

    if (KMLtextContents[indexChar:indexChar+13] == '<coordinates>'):
        indexTemp1 = indexChar

    if (KMLtextContents[indexChar:indexChar+14] == '</coordinates>'):
        coordinateData.append(KMLtextContents[indexTemp1:indexChar + 14])

    if (KMLtextContents[indexChar:indexChar+12] == '</Placemark>'):
        #End found
        indexEnd.append(indexChar+12)
        i = i +1

stayIndex = []
processed = []

for indexCoord in range(0,len(coordinateData)):
    if coordinateData[indexCoord] not in processed:
        stayIndex.append(indexCoord)
        processed.append(coordinateData[indexCoord])


strOut = KMLtextContents[:indexStart[0]]

for i in stayIndex:
    strOut = strOut + KMLtextContents[indexStart[i]:indexEnd[i]]

strOut = strOut + KMLtextContents[indexEnd[len(indexEnd)-1]:]

##

##

f = open("output.kml","w+")
f.write(strOut)
f.close()


print('##-------------------------##')
print('Removed ' + str(len(coordinateData)-len(stayIndex)) +' items.')
print('File saved as output.kml')
print('##-------------------------##')
