import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import  time
import csv
# https://developers.google.com/maps/documentation/geocoding/overview sample file
#intital list of locations
count=0
start  =  time.time()
latitude = list()
langitude = list()
point = list()
#open file in the system
varanasi_city = input("enter a location file name :  ")

if len(varanasi_city)  < 1 :
    varanasi_city = 'list_loc_404.txt'
locations = open(varanasi_city)
location_list = list()
for location in locations:
    location_list.append(location)

for item in location_list:
    # print(item)
    api_key = False
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    address = item
    if len(address) < 1 : break
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    # print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()
    # print('Retrieved', len(data), 'characters')
    # print(data.decode())
    tree = ET.fromstring(data)
    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text
    # print(latitude)
    # print('lat', lat, 'lng', lng)
    # print(location)
    langitude.append(lng)
    latitude.append(lat)
    point.append(location)
    count+=1
    print(count)


print(point)
print(langitude)
print(latitude)


latitude_file  = open('latitude.txt','a+')
for values in latitude:
    # print(values)
    latitude_file.write(values)
    latitude_file.write('\n')
latitude_file.close()

longitude_file =  open("logitude.txt" ,'w+')
for values in langitude:
    longitude_file.write(values)
    longitude_file.write('\n')
longitude_file.close()

#
# detail_info = []
# for i in latitude :
#     for j in  langitude:
#         for k in  point:
#             if latitude.index(i)== langitude.index(j) == point.index(k) :
#                 value = [k, i, j]
#                 detail_info.append(value)
#
# with open('detail_info.csv', 'w', encoding="ISO-8859-1", newline='') as file:
#     wri = csv.writer(file)
#     wri.writerow(("Location", "Latitude", "Longitude"))
#     wri.writerows(detail_info)
# file.close()

print("number of locations are retrieved " , count)
end = time.time()
print(f"Runtime of the program is {end - start}")