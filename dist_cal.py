# import lib
from math import sin, cos,  radians, atan2, sqrt
import numpy,xlsxwriter
import matplotlib.pyplot as plt
import csv
import pandas as pd


#intilize values

rad_earth = 6373.01

f_lat = input("Enter a file name: ")
if len(f_lat) < 1: f_lat = 'latitude.txt'

f_lang = input("Enter a file name: ")
if len(f_lang) < 1 : f_lang = 'logitude.txt'

f_location = input("Enter a file name: ")
if len(f_location)< 1: f_location = 'list_of_location.txt'

lat = open(f_lat)
long= open(f_lang)
location =  open(f_location)
latitude_list, longitude_list, points_list = ([],[],[])
# print(longitude,latitude,points)
det_lat, det_long, det_list = ([],[],[])
for i in lat :
    latitude = float(i)
    det_lat.append(latitude)
    rad_lat = radians(latitude)
    latitude_list.append(rad_lat)
    # print(latitude_list)
for j in long:
    longitude = float(j)
    det_long.append(longitude)
    rad_long = radians(longitude)
    longitude_list.append(rad_long)

for i in location :
    points_list.append(i)
    det_list.append(i)

count = 0
print(len(longitude_list),len(latitude_list),len(points_list))
print(len(det_long),len(det_lat),len(det_list))
detail_info = []
for i in det_lat :
    for j in  det_long:
        for k in  det_list:
            if det_lat.index(i) == det_long.index(j) == det_list.index(k) :
                value = [k, i, j]
                detail_info.append(value)
                count+=1
                print(count)
                print(value)
print(detail_info)
#Create a cord file of lat long location fro KMean Calculation
with open('detail_info.csv', 'w', encoding="ISO-8859-1", newline='') as file:
    wri = csv.writer(file)
    wri.writerow(("Location", "Latitude", "Longitude"))
    wri.writerows(detail_info)
file.close()

# creaign anew list
coordinate_radian = []
for i in latitude_list :
    for j in  longitude_list:
        for k in points_list:
            if latitude_list.index(i)  == longitude_list.index(j) ==  points_list.index(k):
                value = [i,j]
                coordinate_radian.append(value)

print('cord',len(coordinate_radian))
print("long",len(longitude_list))
#
 #i[0] = = latitude value in radian i[1] longtitude value in radian for source node
# j[0] = = latitude value in radian j[1] longtitude value in radian for destination node node
count = 0
dist_list = []
for i in coordinate_radian :
    for j in coordinate_radian:
        # print("Sourece", i[0],"Destination",j[0])
        dlat = j[0] - i[0] #ok
        dlon = j[1] - i[1] #ok
        a = (sin(dlat / 2)) ** 2 + cos(i[1]) * cos(j[1]) * (sin(dlon / 2)) ** 2 #ok
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = rad_earth * c
        count += 1
        mat_size =  int(sqrt(count))
        # distance =("{:.6f}".format(float(distance)))
        dist_list.append(distance)
# print(len(dist_list))
# print(dist_list)
print(len(dist_list))
pair = []
paircount= 0
# for source and destination pair
for source in points_list:
    for destination in points_list:
        paircount+=1
        locality = [source, destination]
        pair.append(locality)
print(len(pair))
with open('distancevalue.csv', 'w', encoding="ISO-8859-1", newline='') as file:
    wri = csv.writer(file)
    wri.writerow(("source", "destination"))
    wri.writerows(pair)
file.close()

df = pd.read_csv("distancevalue.csv")
df['Distance'] = dist_list
df.to_csv("distancevalue.csv", index=False)

dist_mat = numpy.array(dist_list)
size = (mat_size,mat_size)
create_ones = numpy.ones(size)
numpy.set_printoptions(threshold=numpy.inf)
final_mat = dist_mat.reshape(mat_size,mat_size)


workbook = xlsxwriter.Workbook('dist_mat_xlx.xlsx')
worksheet = workbook.add_worksheet()
array =  final_mat
row = 0
for col, data in enumerate(array):
    worksheet.write_column(row, col, data)
workbook.close()


print("Check detail_info.csv for Kmeans calculation")
print("refer values of Distancevalue.csv for more source to destination desination")
print("distance matrix avaliable at dist_mat_xlx.xlxs")
