from math import sin, cos,  radians, atan2, sqrt
import numpy
import csv
import pandas as pd

locationlist= []
cluster = ["cluster1.csv","cluster2.csv","cluster3.csv","cluster4.csv","cluster5.csv","cluster6.csv"]
for item in cluster:
    df = pd.read_csv(item)
    df =pd.read_csv(item)

    df.head()
    latitude = df.Latitude
    longitude = df.Longitude
    rating = df.Rating
    location = df.Location
    latitude_list, longitude_list = ([], [])
    for i in latitude:
        lat = float(i)
        # det_lat.append(latitude)
        rad_lat = radians(lat)
        latitude_list.append(rad_lat)
        # print(latitude_list)
    for j in longitude:
        long = float(j)
        # det_long.append(longitude)
        rad_long = radians(long)
        longitude_list.append(rad_long)
    # print("Latitude", latitude_list)
    # print("Longitude", longitude_list)

    coordinate_radian = []
    for i in latitude_list:
        for j in longitude_list:
            if latitude_list.index(i) == longitude_list.index(j):
                value = [i, j]
                coordinate_radian.append(value)

    rad_earth = 6371.03
    # i[0] = = latitude value in radian i[1] longtitude value in radian for source node
    # j[0] = = latitude value in radian j[1] longtitude value in radian for destination node node
    count = 0
    dist_list = []
    for i in coordinate_radian:
        for j in coordinate_radian:
            # print("Sourece", i[0],"Destination",j[0])
            dlat = j[0] - i[0]  # ok
            dlon = j[1] - i[1]  # ok
            a = (sin(dlat / 2)) ** 2 + cos(i[1]) * cos(j[1]) * (sin(dlon / 2)) ** 2  # ok
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = rad_earth * c
            count += 1
            mat_size = int(sqrt(count))
            # distance =("{:.6f}".format(float(distance)))
            dist_list.append(distance)
    # print(dist_list)

    dist_mat = numpy.array(dist_list)
    size = (mat_size, mat_size)
    numpy.set_printoptions(threshold=numpy.inf)
    final_mat = dist_mat.reshape(mat_size, mat_size)
    # print(final_mat)
    valcount = 0
    valroww = []
    for value in dist_mat:
        valcount += 1
        if valcount > mat_size:
            break
        valroww.append(value)

    valrow = numpy.array(valroww)
    rate = numpy.array(rating)
    product1 = valrow * rate
    # print(product1)
    product = list(product1)
    location_name = (product.index(max(product)))
    # print(location_name)
    keylocation = (location[location_name])
    locationlist.append(keylocation)
    locationlist.append("\n")
print(locationlist)
