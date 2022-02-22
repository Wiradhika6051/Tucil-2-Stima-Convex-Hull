import numpy as np
class MyComplexHull:
    def __init__(self,coordinates):
        self.coordinates = coordinates
        self.simplices = self.getConvexHull(coordinates)

    def sort(self,coordinates):
        #pake quicksort
        if len(coordinates)>1:
            k = self.partisi(coordinates)
            left = self.sort(coordinates[0:k+1])
            right = self.sort(coordinates[k+1:len(coordinates)])
            coordinates = np.concatenate((left,right))
        return coordinates

    def partisi(self,coordinates):
        #buat partisi larik
        #sort dari x nya dulu
        pivot_idx = len(coordinates)//2 
        pivot = coordinates[pivot_idx]
        p = 0
        q = len(coordinates)-1
        while p<=q:
            while coordinates[p][0] < pivot[0]:
                p += 1
            while coordinates[q][0] > pivot[0]:
                q -=1
            if p<=q:
                coordinates[[p,q]] = coordinates[[q,p]]
                p+=1
                q-=1
        return q

    def getConvexHull(self,coordinates):
        #dapetin list convexhull
        sorted_coordinates = self.sort(coordinates)
        start = coordinates[0]
        end = coordinates[-1]
        left = []
        right = []
        for i in range(len(coordinates)):
            check_position = self.checkPosition(start,end,coordinates[i])
            if(check_position>0):
                #kalo positif berarti di kiri
                left.append(coordinates[i])
            elif(check_position<0):
                #kalo negatif berarti di kanan
                right.append(coordinates[i])
            #kalo misal 0 berarti bisa diabaikan(karena segaris)
        simplices = [coordinates[0]]
        simplices.append(self.searchConvexHull(left))
        simplices.append(self.searchConvexHull(right))
        simplices.append(coordinates[-1])
        return simplices

    def searchConvexHull(self,coordinates):
        pass

    def checkPosition(p1,p2,p3):
        #p1->titik paling kiri
        #p2->titik paling kanan
        #p3->titik yang ingin diuji
        #[0]->x
        #[1]->y
        return p1[0]*p2[1]+p3[0]*p1[1]+p2[0]*p3[1]-p3[0]*p2[1]-p2[0]*p1[1]-p1[0]*p3[1]

if __name__=='__main__':
    arrays = np.array([[1,3],[1,2],[3,1],[2,2],[4,1],[-1,2],[0,5],[1,1]])
    hull = MyComplexHull(arrays)
    hull.sort(arrays)
    print(arrays)