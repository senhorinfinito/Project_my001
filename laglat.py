import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET, csv
import ssl
import  time


#intital list of locations count and create empty lists(string_array)

count=0
start  =  time.time()
latitude = list()
langitude = list()
point = list()


#open file in the system
varanasi_city = input("enter a location file name :  ")
#condtion if file name is not provided
if len(varanasi_city)  < 1 :
    varanasi_city = 'list_of_location.txt'
locations = open(varanasi_city)
location_list = list()

# read through each line of file(line contain a single location)
for location in locations:
    location_list.append(location)


for item in location_list:
    # api_key ="your_google_api_key"
    api_key = False
    api_key = 42
    #     #  below link redirect our location to google map with free of cost
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
    # Ignore SSL certificate errors (secure socket layer)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    address = item
    # if file having empty line break the process
    if len(address) < 1 : break
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    # convert input data into utf8 format using urllib.parse.urlencode(parms)
    url = serviceurl + urllib.parse.urlencode(parms)
    # print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()
    # print('Retrieved', len(data), 'characters')
    # print(data.decode())
    tree = ET.fromstring(data)
    # data import XML file
    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text
    # print(latitude)
    # print('lat', lat, 'lng', lng)
    # print(location)
    # Append data into lists of string
    langitude.append(lng)
    latitude.append(lat)
    point.append(location)
    count+=1
    print(count)


print(point)
print(langitude)
print(latitude)

#store output in opratable file
latitude_file  = open('latitude.txt','w+')
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



print("number of locations are retrieved " , count)
print("Both file latitude.txt and longitude.txt are input of further process")
end = time.time()
print(f"Runtime of the program is {end - start}")