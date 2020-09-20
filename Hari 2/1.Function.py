# # mendefinisikan fungsi
# def fungsi():
#     print("ini adalah fungsi")
#
# # memanggil fungsi
# fungsi()

# membuat fungsi sederhana

def belajar():
    print("belajar python")

def biayaBelajar():
    belajar()
    print("biaya belajar python adalah Rp.100000 ")

# membuat fungsi dengan input argumen
def materiPython(modul):
    # belajar()
    biaya = 100000
    totalBiaya = modul * biaya
    print('total biaya',modul , 'modul python adalah Rp.',totalBiaya)

biayaBelajar()
materiPython(5)