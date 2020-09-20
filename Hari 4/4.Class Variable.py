class mahasiswa():

    # class variable = variable yang dimiliki class
    jumlah_mahasiswa = 0

    def __init__(self,input_nama,input_nim):
        # public
        self.nama = input_nama
        self.nim = input_nim
        mahasiswa.jumlah_mahasiswa += 1

otong = mahasiswa("si otong",17010197)
ucup = mahasiswa("si ucung", 1701099)
cebong = mahasiswa('si cebong', 17010200)

print(mahasiswa.jumlah_mahasiswa)