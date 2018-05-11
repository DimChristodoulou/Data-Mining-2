import pandas as pd
from ast import literal_eval
import gmplot
from math import radians, cos, sin, asin, sqrt
from dtw import dtw

"""
Calculate the great circle distance between two points
on the earth (specified in decimal degrees)
"""
def haversine(lon1, lat1, lon2, lat2):

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

testSet = pd.read_csv(
	'test_set_a1.csv', # replace with the correct path
)

trainSet = pd.read_csv(
	'train_set.csv', # replace with the correct path
	converters={"Trajectory": literal_eval},
	index_col='tripId'
)


'''
Start writing the html map files. Every file is named 'index'map.html
'''
#j is used as an index and is parsed as a string to name the map file.
j=0
for i in trainSet.index:
    #Getting 5 rows from the dataframe; could be any five.
    if(i==1 or i==2 or i==4 or i==5 or i==6):
        j+=1
        latitudes = []
        longitudes = []
        for item in trainSet.loc[i,'Trajectory']:
        	longitudes.append(item[1])
        	latitudes.append(item[2])
        #Creating a Google Map Plotter with starting coords 53.383015, -6.237581 and initial zoom equal to 10x.
        gmap = gmplot.GoogleMapPlotter(53.383015, -6.237581, 10)
        #Plotting the path defined by the list of [latitude, longitude] pairs above.
        gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
        name = str(j) + "map.html"
        gmap.draw(name)
'''
End of writing the html map files
'''
