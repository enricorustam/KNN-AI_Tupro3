import numpy
import csv
import math;
import statistics as stat
from math import *

def ng(a,b,c,d,e,f,g,h,i,j):
    return math.sqrt((a - b)**2 + (c - d)**2 + (e - f)**2 + (g - h)**2 + (i - j)**2)

def countK(j):
    return 4*j+1

def uji(DL, DU, k):
    pu = 0
    final = []
    while(pu<200):
        hasil = []
        pl = 0
        while(pl<800):
            count = ng(DU[pu][1],DL[pl][1],DU[pu][2],DL[pl][2],DU[pu][3],DL[pl][3],DU[pu][4],DL[pl][4],DU[pu][5],DL[pl][5])
            nilai = {
                    "nomor" : int(DL[pl][0]-1),
                    "nilai" : count
                }
            hasil.append(nilai)
            pl+=1
        hasil.sort(key=lambda x: x['nilai'])
        n=0
        a = 0
        b = 0
        c = 0
        d = 0
        while True:
            if(n==k):
                break
            else:
                val = int(DL[hasil[n]['nomor']][6])
                if(val==0):
                    a = a + 1
                elif(val==1):
                    b = b + 1
                elif(val==2):
                    c = c + 1
                elif(val==3):
                    d = d + 1
                n+=1
        if(a>b and a>c and a>d):
            final.append(0)
        elif(b>a and b>c and b>d):
            final.append(1)
        elif(c>a and c>b and c>d):
            final.append(2)
        elif(d>a and d>b and d>c):
            final.append(3)
        pu+=1
    a = numpy.asarray(final)
    a.tofile('Final.csv',sep='\n',format='%10.5f')            

def main():
    DL = numpy.genfromtxt("DataTrain_Tugas3_AI.csv",delimiter=',', skip_header=True)
    DU = numpy.genfromtxt("DataTest_Tugas3_AI.csv",delimiter=',', skip_header=True) 
    
    l=0
    m=0
    hv = 0
    ha = 0
    while(l<4):
        m = countK(l)
        k = 0
        baf = 0
        btf = 199
        hk=0
        while(k<=3):
            benar=0
            j = baf
            while(j<=btf):
                cek = []
                nilai = []
                i = 0
                if(baf==0):
                    i = i + 200
                while(i<800):
                    if(i==baf and btf==799):
                        break
                    elif(i==baf and btf!=799):
                        i+=200
                        count = ng(DL[j][1],DL[i][1],DL[j][2],DL[i][2],DL[j][3],DL[i][3],DL[j][4],DL[i][4],DL[j][5],DL[i][5])
                        hasil = {
                                "nomor" : int(DL[i][0]),
                                "nilai" : count
                            }
                        cek.append(hasil)
                        i+=1
                    else:
                        count = ng(DL[j][1],DL[i][1],DL[j][2],DL[i][2],DL[j][3],DL[i][3],DL[j][4],DL[i][4],DL[j][5],DL[i][5])
                        hasil = {
                                "nomor" : int(DL[i][0]-1),
                                "nilai" : count
                            }
                        nilai.append(hasil)
                        i+=1
                nilai.sort(key=lambda x: x['nilai'])
                n = 0
                a=0
                b=0
                c=0
                d=0
                z=0
                while True:
                    if(n==m):
                        break
                    else:
                        val = int(DL[nilai[n]['nomor']][6])
                        if(val==0):
                            a = a + 1
                        elif(val==1):
                            b = b + 1
                        elif(val==2):
                            c = c + 1
                        elif(val==3):
                            d = d + 1
                        n+=1
                if(a>b and a>c and a>d):
                    z=0
                elif(b>a and b>c and b>d):
                    z=1
                elif(c>a and c>b and c>d):
                    z=2
                elif(d>a and d>b and d>c):
                    z=3
                j+=1
                o = int(DL[j-1][6])
                if(o==z):
                    benar+=1
            hk = hk + (benar/200*100)
            k+=1
            baf+=200
            btf+=200
        hv = hk/4
        if(hv>ha):
            ha = hv
            kAkhir = m
        l+=1

    print('akurasi :', ha)
    print('nilai k :', kAkhir)
    uji(DL, DU, kAkhir)
    print('hasil akhir data bisa di lihat pada file Final.csv')

main()
