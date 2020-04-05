P = [2,8,15,23,37]
Q = [4,6,15,20]

def gabungkanlisturut(a,b):
    la = len(a)
    lb = len(b)
    c = list()
    i = 0
    j = 0
    while i < la and j < lb:
        if a[i]< b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    while i < la:
        c.append(a[i])
        i+=1
    while j < lb:
        c.append(b[j])
        j+=1
    return c
print("P =", P)
print("Q = ",Q)
print("gabung dan urutkan q")
print(gabungkanlisturut(P,Q))


def mergesort(A):
    if len(A)>1:
        mid = len (A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]
        mergesort(separuhkiri)
        mergesort(separuhkanan)
        i = 0 ; j = 0 ; k = 0
        while i < len(separuhkiri) and j < len(separuhkanan):
            if separuhkiri[i] < separuhkanan[j]:
                A[k]= separuhkiri[i]
                i+=1
            else:
                A[k] = separuhkanan[j]
                j+=1
            k+=1
        while i < len(separuhkiri):
            A[k] = separuhkiri[i]
            i+=1
            k+=1
        while j< len(separuhkanan):
            A[k] = separuhkanan[j]
            j+=1
            k+=1


alist = [54,26,93,17,77,31,44,55,20]
print("===================================")
print("a = ",alist)
mergesort(alist)
print("urutkan a : ",alist)
print("===================================")

def partisi(A,awal,akhir):
    nilaipivot = A[awal]
    penandakiri = awal + 1
    penandakanan = akhir
    selesai = False

    while not selesai:
        while penandakiri <= penandakanan and A[penandakiri] <= nilaipivot:
            penandakiri +=1
        while A[penandakanan] >= nilaipivot and penandakanan >= penandakiri :
            penandakanan -=1
        if penandakanan < penandakiri:
            selesai = True
        else:
            temp = A[penandakiri]
            A[penandakiri] = A[penandakanan]
            A[penandakanan] = temp
    temp = A[awal]
    A[awal] = A[penandakanan]
    A[penandakanan] = temp

    return penandakanan


def quicksortbantu(A,awal,akhir):
    if awal < akhir:
        titikbelah = partisi(A,awal,akhir)
        quicksortbantu(A,awal,titikbelah -1)
        quicksortbantu(A,titikbelah+1,akhir)

def quicksort(A):
    quicksortbantu(A,0,len(A)-1)
    
z = [41,23,21,23,4,5,67,37]
print("z : ",z)
quicksort(z)
print("urutkan z :",z)
