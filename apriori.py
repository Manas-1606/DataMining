import pandas as pd
import numpy as np
from itertools import combinations

arr=[]   # Stores list of all combinations
freq={}  # Stores frequency of final combinations after pruning based on min support
all={} # Stores frequency of all combinations
# Transaction dataset
dict={
    1:['A','B','E'],
    2:['B','D'],
    3:['B','C'],
    4:['A','B','D'],
    5:['A','C'],
    6:['B','C'],
    7:['A','C'],
    8:['A','B','C','E'],
    9:['A','B','C'],

}

# To prune based on min support
def prune(delist,min):
    for i in freq:
        if(freq[i]<min):
            delist.append(i);
    for i in delist:
        del freq[i]


# To initialize frequency of all combinations to 0
def freqinit():
    for i in arr:
        for j in i:
            str=""
            for k in j:
                str=str+k
            freq[str]=0;


# To find frequency of combination
def findfreq(tempset):
    for i in tempset:
        str=""
        flag=True
        for j in i:
            str=str+j
        for d in dict:
            flag=True
            for s in str:
                if(s not in dict[d]):
                    flag=False
                    break
            if(flag==True):
                freq[str]=freq[str]+1
# To generate combinations
def generate(dict,init,k):
    tempset=[]
    n=combinations(init,k+1)
    n1 = [''.join(i) for i in n]

    for i in n1:
        tset=set()
        for j in i:
            tset.add(j)
        tempset.append(tset)

    arr.append(tempset)





init=[]
delist=[]
min=2
for i in dict:
    for j in dict[i]:

        init.append(j)

m=set(init)
# Generating sets of combinations
for i in range(len(m)):
    c=generate(dict,m,i)


# Initialising the frequency of each item with 0
freqinit()

# Updating the frequency of the items
for i in arr:
    findfreq(i)

for i in freq:
    all[i]=freq[i]

# Pruning based on min support
prune(delist,min)




print(all)
print(freq)
