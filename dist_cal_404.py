# import lib
from math import sin, cos,  radians, atan2, sqrt
import numpy
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
if len(f_location)< 1: f_location = 'list_loc_497.txt'

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

detail_info = []
for i in det_lat :
    for j in  det_long:
        for k in  det_list:
            if det_lat.index(i)== det_long.index(j) == det_list.index(k) :
                value = [k, i, j]
                detail_info.append(value)

#Create a cord file of lat long location
# with open('detail_info.csv', 'w', encoding="ISO-8859-1", newline='') as file:
#     wri = csv.writer(file)
#     wri.writerow(("Location", "Latitude", "Longitude"))
#     wri.writerows(detail_info)
# file.close()

# creaign anew list
coordinate_radian = []
for i in latitude_list :
    for j in  longitude_list:
          if latitude_list.index(i)== longitude_list.index(j) :
                value = [i,j]
                coordinate_radian.append(value)
print(len(latitude_list))
print(len(longitude_list))
print(len(coordinate_radian))
# for k in points_list:
#     for latlong in values:
#         if points_list.index(k) == values.index(latlong):
#             print(k,latlong)
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

pair = []
paircount= 0
# for source and destination pair
for source in points_list:
    for destination in points_list:
        paircount+=1
        locality = [source, destination]
        pair.append(locality)


with open('Locationdet_value.csv', 'w', encoding="ISO-8859-1", newline='') as file:
    wri = csv.writer(file)
    wri.writerow(("source", "destination"))
    wri.writerows(pair)
file.close()

with open("distpointopoint.txt", "w") as output:
    for number in dist_list:
        output.write(str(number))
        output.write('\n')

# with open('Locations_value.csv', 'w', encoding="ISO-8859-1", newline='') as file:
#     wri = csv.writer(file)
#     wri.writerow(("Dist"))
#     wri.writerows(dist_list)
# file.close()
#         if pair.index(pairpose) == dist_list.index(distpos):
#             eac_dis= [pairpose,distpos]
#             lineup.append(eac_dis)
#             lineupcount += 1
#             print(lineupcount)
#         if (lineupcount) > 7000:
#             break
# print(lineup)


# for point in pair:
#     for dist in dist_list:
#         if pair.index(point)== dist_list.index(dist):
#             print(point,dist)


# # dist_mat = numpy.array(dist_list)
# size = (mat_size,mat_size)
# create_ones = numpy.ones(size)
# numpy.set_printoptions(threshold=numpy.inf)
# final_mat = dist_mat.reshape(mat_size,mat_size)

# numpy.savetxt('dist_mat.txt',final_mat)

# x_axes = range[1,mat_size,1]
# y_axes = (final_mat[0])
# plt.scatter(x_axes,y_axes)
# plt.show()
