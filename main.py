"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

from myComplexHull import MyComplexHull
data = datasets.load_iris()
#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.shape)
df.head()

#visualisasi hasil ConvexHull
from scipy.spatial import ConvexHull
plt.figure(figsize = (10, 6))
colors = ['b','r','g'] 
plt.title('Petal Width vs Petal Length')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    hull = ConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for sim in hull.simplices:
        print("sim1:",i,sim)
    print(i,bucket,len(bucket))
    for simplex in hull.simplices:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import myComplexHull as my
from sklearn import datasets
data = datasets.load_iris()
#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.shape)
df.head()

#visualisasi hasil ConvexHull
#from scipy.spatial import ConvexHull
plt.figure(figsize = (10, 6))
#colors = ['b','r','g'] 
plt.title('Petal Width vs Petal Length')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
#for i in range(1):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    hull = my.MyComplexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i],c=hull.color)
    #print("hull:",hull.simplices)
    for simplex in hull.simplices:
        #plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], hull.color)

plt.legend()
plt.show()
"""
import pandas as pd
import matplotlib.pyplot as plt
import myComplexHull as my
from sklearn import datasets
data = datasets.load_breast_cancer()
#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.shape)
df.head()

#visualisasi hasil ConvexHull
#from scipy.spatial import ConvexHull
plt.figure(figsize = (10, 6))
#colors = ['b','r','g'] 
plt.title('Radius vs Texture')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
#for i in range(1):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    hull = my.MyComplexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i],c=hull.color)
    #print("hull:",hull.simplices)
    for simplex in hull.simplices:
        #plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], hull.color)

plt.legend()
plt.show()