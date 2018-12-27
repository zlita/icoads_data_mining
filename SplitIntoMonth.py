import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import folium
import datetime


CHUNKSIZE = 50000

#sea_surface_temp, sea_level_pressure
data = pd.read_csv("resultat_total_2005.csv",chunksize=CHUNKSIZE)
pd.set_option('display.max_columns', None)
#print(data.head(10))

janvier = []
fevrier = []
mars = []
avril = []
mai = []
juin = []
juillet = []
aout = []
septembre = []
octobre = []
novembre = []
decembre = []
for chunk in data:
    for index, row in chunk.iterrows():
        try:
            storedTime = datetime.datetime.strptime(row["timestamp"][:-6], "%Y-%m-%d %H:%M:%S")
            if index % 1000000 == 0:
                print(index)
            #print("storetime : ", storedTime)
        except:
            pass
        else:
            # print("storetime : ", storedTime)
            # print("MONTH :", storedTime.month)
            if storedTime.month == 1:
                janvier.append(row)
            elif storedTime.month == 2:
                fevrier.append(row)
            elif storedTime.month == 3:
                mars.append(row)
            elif storedTime.month == 4:
                avril.append(row)
            elif storedTime.month == 5:
                mai.append(row)
            elif storedTime.month == 6:
                juin.append(row)
            elif storedTime.month == 7:
                juillet.append(row)
            elif storedTime.month == 8:
                aout.append(row)
            elif storedTime.month == 9:
                septembre.append(row)
            elif storedTime.month == 10:
                octobre.append(row)
            elif storedTime.month == 11:
                novembre.append(row)
            elif storedTime.month == 12:
                decembre.append(row)
            else:
                pass

janvier = np.array(janvier)
fevrier = np.array(fevrier)
mars = np.array(mars)
avril = np.array(avril)
mai = np.array(mai)
juin = np.array(juin)
juillet = np.array(juillet)
aout = np.array(aout)
septembre = np.array(septembre)
octobre = np.array(octobre)
novembre = np.array(novembre)
decembre = np.array(decembre)
name = 1
month = [janvier, fevrier, mars, avril, mai, juin, juillet, aout, septembre, octobre, novembre, decembre]
for i in month:
    df = pd.DataFrame(i)
    title = "{}.csv".format(name)
    df.to_csv(title)
    name += 1
