import haversine as hs   
from haversine import Unit

start = [(-6.914224, 112.828577), (0,0), (0,0), (0,0), (0,0)]
stop = [(-7.017114, 112.905483), (0,0), (0,0), (0,0), (0,0)]
dist = []
tot_dist = 0

for i in range(len(start)):
    dist.append(hs.haversine(start[i], stop[i], unit=Unit.KILOMETERS))
    tot_dist += dist[i]
 
print("The distance calculated is:", round(tot_dist))
print("Number of station is: ", round(tot_dist/1.4))