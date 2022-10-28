
import math


n = int(input("Enter number of points: "))

listed = []
co_ords = []
centroids = []
distances = []
lst = []
min_list = []

#Taking input from user
for i in range(1, n+1):
    print("For point ", i, ": ")
    x = int(input("X co-ordinate: "))
    y = int(input("Y co-ordinate: "))
    point = list([x,y])
    co_ords.append(point)




#Choosing initial centroids
k = int(input("Number of clusters required: "))
print("Choose centroids: ")
for i in range(0, k):
    print("Centroid ", i, ": ")
    x = int(input("X co-ordinate: "))
    y = int(input("Y co-ordinate: "))
    ctr = list([x,y])
    centroids.append(ctr)


t = int(input("enter no. of iterations: "))
for it in range(t):
    #Function to calculate Eucledian Distance
    def distance(x, y):
        x1 = x[0]
        x2 = y[0]
        y1 = x[1]
        y2 = y[1]
        #print(x1, x2, y1, y2)
        ques = ((x2-x1)**2) + ((y2-y1)**2)
        #print(ques)
        return math.sqrt(ques)

    #Calculating distances
    for i in range(0, n):
        for j in range(0, k):
            d1 = (distance(co_ords[i], centroids[j]))
            lst.append(d1)
        distances.append(list(lst))
        lst.clear()




    #Finding minimum distance and which cluster it is closer to
    for i in range(0, n):
        mini = distances[i][0]
        min_index = 0
        for j in range(0, k):
            if(distances[i][j] < mini):
                mini = distances[i][j]
                min_index = j
        min_list.append(min_index)


    print("Eucledian distances: ", distances)
    print("Co-ordinates: ", co_ords)
    print("Old centroids: ", centroids)
    print("Cluster classification: ", min_list)



    j = 0
    while (j < k):
        lsts = []
        for i in range(0, n):
            
            if(min_list[i] == j):
                lsts.append(co_ords[i])
        size = len(lsts)
        print(lsts)
        x_sum = 0
        y_sum = 0
        if(size > 0):
            for l in range(0, size):
                x_sum = x_sum + lsts[l][0]
                y_sum = y_sum + lsts[l][1]
            x_mean = x_sum/size
            y_mean = y_sum/size
            new_ctr = list([x_mean, y_mean])
            #print(x_mean, y_mean)
            centroids[j] = new_ctr
        
        j= j + 1

    min_list.clear()
    print("New centroids: ", centroids)








