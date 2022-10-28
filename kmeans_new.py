#K-Means algorithm

import matplotlib.pyplot as plt


# Find Distance from centroid and point
def dis(c,d):
    distance=abs(d[0]-c[0])+abs(d[1]-c[1])
    return distance

# Calculate new Centroid by calculating mean
def findCentroid(cluster):
    tempcent=[]
    for i in cluster:
        xsum=0
        ysum=0
        x=0
        y=0
        length=len(i)
        for j in i:
            xsum=xsum+j[0]
            ysum=ysum+j[1]
        x=xsum/length
        y=ysum/length
        tempcent.append((x,y))
    return tempcent

data_points=[]
cluster=[]
centroids=[]

print("Enter number of points :",end=' ')
n=int(input())
print("Enter number of clusters :",end=' ')
k=int(input())
print("Enter the points :",end=' ')

# Adding data points to data_points
for i in range(n):
    l=int(input())
    m=int(input())
    t=(l,m)
    data_points.append(t)

print("Enter the centroid points :",end=' ')

# Adding centroid points to centroids variable
for i in range(k):
    l=int(input())
    m=int(input())
    t=(l,m)
    centroids.append(t)
    cluster.append([])

flag=True

# While look runs until there is no change in centroid
while(flag==True):
    for i in data_points:
        tempclus=[] #stores the distance of a point from each centroid
        for j in centroids:
            d=dis(j,i)
            tempclus.append(d)
        min=99999
        pos=-1
        for j in range(len(tempclus)):
            if(tempclus[j]<min): #checks distance to which centroid is minimum
                min=tempclus[j]
                pos=j
        if(i not in cluster[pos]): #Adds the point with minimum distance to centroid to that cluster if it is already not present
            cluster[pos].append(i)

    new=findCentroid(cluster) #calculates new centroid
    if(new==centroids): #checking if newly calculated centroid is same as old one
        break;
    else:
        centroids=new

print(cluster)

for i in cluster:
    x=[]
    y=[]
    for j in i:
        x.append(j[0])
        y.append(j[1])
    plt.scatter(x,y)
plt.show()