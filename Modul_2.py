##Soal 1
class Pesan(object):
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def apakahTerkandung(self,x):
        if x in self.teks:
            return True
        else:
            return False
    def hitungKonsonan(self):
        kon = 0
        vokal = 'aiueoAIUEO'
        for i in self.teks:
            if i not in vokal:
                kon +=1
        return kon
    def hitungVokal(self):
        vok = 0
        vokal = 'aiueoAIUEO'
        for i in self.teks:
            if i in vokal:
                vok +=1
        return vok

##Soal 2
class Manusia(object):
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('salam, namaku', self.nama)
    def makan(self,s):
        print('saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self,k):
        print('saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self,n):
        return n*2

class Mahasiswa(Manusia):
    def __init__(self, nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + ', Tinggal di ' + self.kotaTinggal \
            + ', Uang Saku Rp ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def tambahUangSaku(self,tambahUang):
        self.uangSaku = self.uangSaku + tambahUang
    def makan(self,s):
        print("Saya baru saja makan", s , "sambil belajar")
        self.keadaan = 'kenyang'
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self,kotaBaru):
        self.kotaTinggal = kotaBaru

##Soal 3
##a = input('Masukkan Nama : ')
##b = input('Masukkan NIM : ')
##c = input('Masukkan Kota Tinggal : ')
##d = input('Masukkan Uang Saku per Bulan : ')
##x = Mahasiswa(a,b,c,d)
##print('Data Mahasiswa : ',x)

##Soal 4 dan 5
class Manusia(object):
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('salam, namaku', self.nama)
    def makan(self,s):
        print('saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self,k):
        print('saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self,n):
        return n*2

class Mahasiswa(Manusia):
    def __init__(self, nama,NIM,kota,us,lk=[]):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.lk = lk
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + ', Tinggal di ' + self.kotaTinggal \
            + ', Uang Saku Rp ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def tambahUangSaku(self,tambahUang):
        self.uangSaku = self.uangSaku + tambahUang
    def makan(self,s):
        print("Saya baru saja makan", s , "sambil belajar")
        self.keadaan = 'kenyang'
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self,kotaBaru):
        self.kotaTinggal = kotaBaru
        
##Soal 4
    def listKuliah(self):
        return self.lk
    def ambilKuliah(self, ambil):
        self.lk.append(ambil)

##Soal 5
    def hapusKuliah(self,hapus):
        for x in self.lk:
            if hapus in self.lk:
                self.lk.remove(hapus)
            else:
                print("maaf anda tidak dapat menghapus matkul tersebut karena matkul tersebut tidak ada")

##Soal 6
from datetime import date
class Manusia(object):
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('salam, namaku', self.nama)
    def makan(self,s):
        print('saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self,k):
        print('saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self,n):
        return n*2

class SiswaSMA(Manusia):
    def __init__(self, nama, nis, umur, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nis = nis
        self.umur = umur
        self.us = us
        
    def __str__(self):
        s = self.nama +', NIS '+str(self.nis)\
            +'. Berumur '+ str(self.umur) \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap harinya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIS(self):
        return self.nis
    def ambilUmur(self):
        return self.umur
    def ambilUangSaku(self):
        return self.us

    def tahunLahir(self):
        thnskr = date.today().year
        tl = thnskr - self.umur
        return tl

##Soal 7
class MhsTIF(Mahasiswa):
    def katakanPy(self):
        print("python is cool.")
        
            

    
