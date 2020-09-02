# list sebagai iterable
gorengan = ['bakwan','tempe goreng','ubi goreng','tahu goreng']

for g in gorengan:
    print(g)
    print(len(g))

# string sebagai iterable
makan = 'bakwan'
for m in makan:
    print(m)

# for dalam for
print(100*"=")

buah = ['apel','semangka','melon','leci','anggur']
sayuran = ['gubis','tomat','kangkung','mentimun','kelor']

DaftarBelanja = [gorengan,buah,sayuran]

for SubBelanja in DaftarBelanja:
    print(SubBelanja)
    for komponen in SubBelanja:
        print(komponen)