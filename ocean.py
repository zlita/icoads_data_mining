import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import folium

data = pd.read_csv("resultat_total_2005.csv", chunksize=50000)
temp = []

for chunk in data:
    temp.append(chunk[["wave_period", "wave_height","latitude", "longitude"]].dropna())

data = pd.concat(temp)
data = data.head(20000)




kmeans = KMeans(n_clusters=4)
kmeans.fit(data[["wave_period", "wave_height"]])
data2 = kmeans.predict(data[["wave_period", "wave_height"]])
#data2 = pd.DataFrame(y_kmeans)
#data = pd.concat([data, data2])
print(data)


#create a map
this_map = folium.Map(prefer_canvas=True)

def plotDot(points, cluster):
    for point in range(0, len(points)) :
        if cluster[point] == 0 :
            folium.CircleMarker(location=[points.iloc[point]["latitude"], points.iloc[point]["longitude"]],
                            radius=1,
                            weight=0.5, color="red").add_to(this_map)

        elif cluster[point] == 1 :
            folium.CircleMarker(location=[points.iloc[point]["latitude"], points.iloc[point]["longitude"]],
                            radius=1,
                            weight=0.5, color="green").add_to(this_map)

        elif cluster[point] == 2 :
            folium.CircleMarker(location=[points.iloc[point]["latitude"], points.iloc[point]["longitude"]],
                            radius=1,
                            weight=0.5, color="blue").add_to(this_map)
        else :
            folium.CircleMarker(location=[points.iloc[point]["latitude"], points.iloc[point]["longitude"]],
                            radius=1,
                            weight=0.5, color="black").add_to(this_map)



#use df.apply(,axis=1) to "iterate" through every row in your dataframe
plotDot(data,data2)
#data.apply(plotDot, axis = 1)


#Set the zoom to the maximum possible
this_map.fit_bounds(this_map.get_bounds())

#Save the map to an HTML file
this_map.save('cluster_on_map.html')
