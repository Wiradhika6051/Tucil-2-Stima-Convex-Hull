from cmath import sqrt
from operator import le
from tracemalloc import start
from turtle import circle, st
import numpy as np
class MyComplexHull:
    def __init__(self,coordinates):
        self.coordinates = coordinates
        self.simplices = self.getConvexHull(coordinates)

    def sort(self,coordinates,axis=0):#0:x,1:y
        #pake quicksort
        if len(coordinates)>1:
                k,coordinates = self.partisi(coordinates)
                left = self.sort(coordinates[0:k+1])
                right = self.sort(coordinates[k+1:len(coordinates)])
                coordinates = np.concatenate((left,right))
        return coordinates
    def sorty(self,coordinates):
        #sort berdasarkan y agar terurut membesar
        if(len(coordinates)>1):
            final_array= []
            subarr =[coordinates[0]]
            for i in range(1,len(coordinates)):
                if(coordinates[i][0]==subarr[0][0]):
                    #x nya sama
                    subarr.append(coordinates[i])
                else:
                    final_array = final_array +  self.sub_sorty(subarr)
                    subarr = [coordinates[i]]
            if(subarr):
                    final_array = final_array + self.sub_sorty(subarr)
            return final_array
        elif len(coordinates)==1:
            return coordinates
        else:
            return []
    def sub_sorty(self,coordinates):
        #sub fungsi untuk solve sort sumbu y
        if len(coordinates)>1:
                k,coordinates = self.partisi(np.array(coordinates),1)
                coordinates = list(coordinates)
                left = self.sub_sorty(coordinates[0:k+1])
                right = self.sub_sorty(coordinates[k+1:len(coordinates)])
                coordinates = left +right
        return coordinates

    def partisi(self,coordinates,axis=0):#0->x,1->Y
        #buat partisi larik
        #sort dari x nya dulu
        pivot_idx = len(coordinates)//2 
        pivot = coordinates[pivot_idx]
        p = 0
        q = len(coordinates)-1
        while p<=q:
            while p<len(coordinates):
                if(coordinates[p][axis] >= pivot[axis]):
                    break
                p += 1
            while q>=0:
                if coordinates[q][axis] <= pivot[axis]:
                    break
                q -=1
            if p<=q:
                coordinates[[p,q]] = coordinates[[q,p]]
                p+=1
                q-=1
        return (q,coordinates)

    def getConvexHull(self,coordinates):
        #dapetin list convexhull
        temp = np.array([[coordinates[i][0],coordinates[i][1],i] for i in range(len(coordinates))])
        temp1 = self.sort(temp)
        sorted_coordinates = list(self.sorty(temp1))
        start = sorted_coordinates[0]
        end = sorted_coordinates[-1]
        left = []
        right = []
        for i in range(1,len(sorted_coordinates)-1):
            check_position = self.checkPosition(start,end,sorted_coordinates[i])
            if(check_position>0):
                #kalo positif berarti di kiri
                left.append(sorted_coordinates[i])
            elif(check_position<0):
                #kalo negatif berarti di kanan
                right.append(sorted_coordinates[i])
            #kalo misal 0 berarti bisa diabaikan(karena segaris)
        simplices  = [start]
        simplices = simplices + list(self.sorty(self.sort(np.array(self.searchConvexHullUpper(left,start,end)))))
        simplices.append(end)
        convex_kanan = self.searchConvexHullLower(right,start,end)
        for i in range(len(convex_kanan)-1,-1,-1):
            simplices.append(convex_kanan[i])
        simplices_map = []
        simplices = [list(simplice) for simplice in simplices]
        for i in range(len(simplices)):
            n = i 
            n1 = (i+1) % len(simplices)
            map1  = [int(simplices[n][2]),int(simplices[n1][2])]
            simplices_map.append(map1)
        simplices_map = np.array(simplices_map)
        return simplices_map

    def searchConvexHullUpper(self,coordinates,start,end):
        if(len(coordinates)>1):
            #buat nyari di bagian atas
            start_point = start
            end_point = end
            convex_simplices = []
            left = []
            right = []
            #cari titik terjauh
            if(len(coordinates)>1 and not(start[0]==end[0] and start[1]!=end[1])):
                farthet_point,idx = self.getFarthestPoint(coordinates,start,end)
                convex_simplices.append(farthet_point)
                coordinates.pop(idx)
                for j in range(len(coordinates)):
                    if(self.checkPosition(start_point,farthet_point,coordinates[j])>0):
                        left.append(coordinates[j])
                    elif(self.checkPosition(end_point,farthet_point,coordinates[j])<0):
                        right.append(coordinates[j])
                left = list(self.sorty(self.sort(np.array(left))))
                right = list(self.sorty(self.sort(np.array(right))))
                left_simplices = []
                right_simplices = []
                if(len(left)>0):
                    left_simplices = self.searchConvexHullUpper(left,start,farthet_point)
                if(len(right)>0):
                    right_simplices = self.searchConvexHullUpper(right,farthet_point,end)
                convex_simplices = convex_simplices + left_simplices + right_simplices
            else:
                convex_simplices = convex_simplices + coordinates
            return convex_simplices
        elif(len(coordinates)==1):
            return coordinates
        else:
            return []

    def searchConvexHullLower(self,coordinates,start,end):
        if(len(coordinates)>1):
            #buat nyari di bagian bawah
            start_point = start
            end_point = end
            convex_simplices = []
            left = []
            right = []
            #cari titik terjauh
            if(len(coordinates)>1 and not(start[0]==end[0] and start[1]==end[1])):
                farthet_point,idx = self.getFarthestPoint(coordinates,start,end)
                convex_simplices.append(farthet_point)
                coordinates.pop(idx)
                for j in range(len(coordinates)):
                    if(self.checkPosition(start_point,farthet_point,coordinates[j])<0):
                        left.append(coordinates[j])
                    elif(self.checkPosition(end_point,farthet_point,coordinates[j])>0):
                        right.append(coordinates[j])
                left = list(self.sorty(self.sort(np.array(left))))
                right = list(self.sorty(self.sort(np.array(right))))
                left_simplices = []
                right_simplices = []
                if(len(left)>0):
                    left_simplices = self.searchConvexHullLower(left,start,farthet_point)
                if(len(right)>0):
                    right_simplices = self.searchConvexHullLower(right,farthet_point,end)
                convex_simplices = convex_simplices + left_simplices + right_simplices
            else:
                convex_simplices = convex_simplices + coordinates
            return list(self.sort(np.array(convex_simplices)))
        elif(len(coordinates)==1):
            return coordinates
        else:
            return []

    def getFarthestPoint(self,coordinates,start,end):
        #mendapatkan titik terjauh
        idx = 0
        farthest_point = coordinates[0]
        farthest_distance = self.distanceFromLine(start,end,coordinates[0])
        biggest_degree = self.getDegree(start,end,coordinates[0])
        for i in range(len(coordinates)):
            distance = self.distanceFromLine(start,end,coordinates[i])
            degree=self.getDegree(start,end,coordinates[i])
            if(distance>farthest_distance):
                farthest_point = coordinates[i]
                farthest_distance = distance
                biggest_degree = degree
                idx = i
            elif(distance==farthest_distance and degree>biggest_degree):
                farthest_point = coordinates[i]
                farthest_distance = distance
                biggest_degree = degree
                idx = i
        return (farthest_point,idx)

    def distanceFromLine(self,start_point,end_point,check_point):
        #menghitung jarak suatu titik dari garis yg dibentuk oleh start_point dan end_point
        A = end_point[1]-start_point[1]
        B = -(end_point[0]-start_point[0])
        C = start_point[1]*(end_point[0]-start_point[0])-start_point[0]*(end_point[1]-start_point[1])
        return abs(A*check_point[0]+B*check_point[1]+C)/(sqrt(A**2+B**2))

    def getDegree(self,p1,p2,pmain):
        #mendapatkan sudut p1pmainp2 menggunakan aturan cosinus
        c = self.getDistance(p1,p2)
        b = self.getDistance(p1,pmain)
        a = self.getDistance(p2,pmain)
        cosx = (a**2-b**2-c**2)/(-2*b*c)
        return np.arccos(cosx)

    def getDistance(self,p1,p2):
        #mengembalikan jarak antara 2 titik
        return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2).real
        
    def checkPosition(self,p1,p2,p3):
        #p1->titik paling kiri
        #p2->titik paling kanan
        #p3->titik yang ingin diuji
        #[0]->x
        #[1]->y
        return p1[0]*p2[1]+p3[0]*p1[1]+p2[0]*p3[1]-p3[0]*p2[1]-p2[0]*p1[1]-p1[0]*p3[1]

if __name__=='__main__':
    arrays = np.array([[5,2],[1,3],[1,2],[4,4],[3,1],[2,2],[4,1],[-1,2],[0,5],[1,1]])
    hull = MyComplexHull(arrays)
    #arrey = hull.sort(arrays)
    #print(arrey)
    print(hull.simplices)