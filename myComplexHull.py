import util as ut
import numpy as np
class MyComplexHull:
    color_idx = 0
    colors = ['b','r','g','c','m','y','k','#7b3f00']##7b3f00->chocolate
    def __init__(self,coordinates):
        self.coordinates = coordinates
        self.simplices = self.getConvexHull(coordinates)
        self.color = MyComplexHull.colors[(MyComplexHull.color_idx)%len(MyComplexHull.colors)]
        MyComplexHull.color_idx += 1

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
            check_position = ut.checkPosition(start,end,sorted_coordinates[i])
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
                farthet_point,idx = ut.getFarthestPoint(coordinates,start,end)
                convex_simplices.append(farthet_point)
                coordinates.pop(idx)
                for j in range(len(coordinates)):
                    if(ut.checkPosition(start_point,farthet_point,coordinates[j])>0):
                        left.append(coordinates[j])
                    elif(ut.checkPosition(end_point,farthet_point,coordinates[j])<0):
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
                farthet_point,idx = ut.getFarthestPoint(coordinates,start,end)
                convex_simplices.append(farthet_point)
                coordinates.pop(idx)
                for j in range(len(coordinates)):
                    if(ut.checkPosition(start_point,farthet_point,coordinates[j])<0):
                        left.append(coordinates[j])
                    elif(ut.checkPosition(end_point,farthet_point,coordinates[j])>0):
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

if __name__=='__main__':
    arrays = np.array([[5,2],[1,3],[1,2],[4,4],[3,1],[2,2],[4,1],[-1,2],[0,5],[1,1]])
    hull = MyComplexHull(arrays)
    #arrey = hull.sort(arrays)
    #print(arrey)
    print(hull.simplices)