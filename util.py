from cmath import sqrt
import numpy as np
def checkPosition(p1,p2,p3):
    #p1->titik paling kiri
    #p2->titik paling kanan
    #p3->titik yang ingin diuji
    #[0]->x
    #[1]->y
    return p1[0]*p2[1]+p3[0]*p1[1]+p2[0]*p3[1]-p3[0]*p2[1]-p2[0]*p1[1]-p1[0]*p3[1]

def getDistance(p1,p2):
    #mengembalikan jarak antara 2 titik
    return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2).real

def getDegree(p1,p2,pmain):
    #mendapatkan sudut p1pmainp2 menggunakan aturan cosinus
    c = getDistance(p1,p2)
    b = getDistance(p1,pmain)
    a = getDistance(p2,pmain)
    cosx = (a**2-b**2-c**2)/(-2*b*c)
    return np.arccos(cosx)

def distanceFromLine(start_point,end_point,check_point):
    #menghitung jarak suatu titik dari garis yg dibentuk oleh start_point dan end_point
    A = end_point[1]-start_point[1]
    B = -(end_point[0]-start_point[0])
    C = start_point[1]*(end_point[0]-start_point[0])-start_point[0]*(end_point[1]-start_point[1])
    return abs(A*check_point[0]+B*check_point[1]+C)/(sqrt(A**2+B**2))

def getFarthestPoint(coordinates,start,end):
        #mendapatkan titik terjauh
        idx = 0
        farthest_point = coordinates[0]
        farthest_distance = distanceFromLine(start,end,coordinates[0])
        biggest_degree = getDegree(start,end,coordinates[0])
        for i in range(len(coordinates)):
            distance = distanceFromLine(start,end,coordinates[i])
            degree=getDegree(start,end,coordinates[i])
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