# scope variable : local

namaKucing = 'Ilui' # global
makananKucing = 'Ikan Asin'

def ubahNamaKucing(namaBaru):
    global namaKucing # variable global
    namaKucing = namaBaru # variable local
    print('saya ubah nama kucing menjadi', namaKucing)

def kasihMakanKucing(makanan,nama):
    global namaKucing,makananKucing
    namaKucing = nama
    makananKucing = makanan

ubahNamaKucing('Imut')
kasihMakanKucing('Ayam Goreng','Ilui')
print('nama kucing saya menjadi',namaKucing,'dan makanan nya', makananKucing)