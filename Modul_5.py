class MhsTIF(object):
    def __init__(self,nama,nim,tinggal,us):
        self.nama = nama
        self.nim = nim
        self.tinggal = tinggal
        self.us = us

c0 = MhsTIF('Wulandari', "L200180091", 'Sukoharjo', 500000)
c1 = MhsTIF('Nayu', "L200180099", 'Kalimantan', 125000)
c2 = MhsTIF('Irul', "L200180101", 'Riau', 450000)
c3 = MhsTIF('Caca', "L200180097", 'Bekasi', 350000)
c4 = MhsTIF('Berlin', "L200180107", 'Pati', 450000)
c5 = MhsTIF('Abid', "L200180059", 'Wonogiri', 350000)
c6 = MhsTIF('Ayud', "L200180095", 'Surakarta', 250000)
c7 = MhsTIF('Rama', "L200180065", 'Sragen', 150000)
c8 = MhsTIF('Fandit', "L200180118", 'Sragen', 250000)
c9 = MhsTIF('Elsa', "L200180108", 'Sukoharjo', 350000)

Daftar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]
        
################################## nomer1 ######################################
def swap(a,b,c):
    tmp=a[b]
    a[b]=a[c]
    a[c]=tmp
    
def cekNIM(Daftar):
    for i in Daftar:
        print(i.nama,i.nim,i.tinggal)

def urutNIM(a):
    n = len(a)
    for x in range(n-1):
        for y in range(n-x-1):
            if a[y].nim > a[y+1].nim:
                swap(a,y,y+1)
################################## nomer2 ######################################
a = [18, 13, 44, 25, 66, 107, 78, 89]
b = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

#pendek
def urutC(a,b):
    c = a +b
    for i in range(1,len(c)):
        nilai = c[i]
        pos = i
        while pos >0 and nilai<c[pos - 1]:
            c[pos]= c[pos-1]
            pos -= 1
        c[pos] = nilai
    print(c)

#panjang
def urutc(a,b):
    pan1 = len(a)
    pan2 = len(b)
    x= 0
    y=0
    c = []
    while x< pan1 and y<pan2:
        if a[x]<b[y]:
            c.append(a[x])
            x += 1
        else:
            c.append(b[y])
            y += 1
    while x<pan1:
        c.append(a[x])
        x += 1
    while y<pan2:
        c.append(b[y])
        y += 1
    return c

################################ nomer3 ######################################
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak=detak();print("Bubble    : %g detik"%(ak-aw));
aw = detak();selectionSort(u_sel);ak=detak();print("Selection : %g detik"%(ak-aw));
aw = detak();insertionSort(u_ins);ak=detak();print("Insertion : %g detik"%(ak-aw));

