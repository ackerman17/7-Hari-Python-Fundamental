Barang = ['hoodie','jaket','mobil','motor','laptop']

# method untuk manipulasi list

# method tambah data
Barang.append('sepeda')
print(Barang)

Barang.extend("Dompet")
print(Barang)

Barang.insert(3,"Tas")
print(Barang)

# method untuk menghitung anggota
jumlahSepeda = Barang.count("sepeda")
print("jumlah sepeda:",jumlahSepeda)

# remove data
Barang.remove('sepeda')
print(Barang)

Barang.reverse()
print(Barang)

print(100*"=")
Stuff = Barang.copy()
Stuff.append('gelas')
print(Stuff)
print(Barang)