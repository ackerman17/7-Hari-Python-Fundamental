# input output file


"""
w = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka dibuat file baru
r = read mode only / hanya bisa baca
a = appending mode / menambahkan data di akhir baris
r+ = write and read mode
"""

# membuat file text
file = open("data.txt",'w')
file.write("ini adalah data text")
file.write("\n ini baris kedua")
file.write("\n ini baris ketiga")
file.write("\n ini baris keempat")
file.close()

# membaca file text
file2 = open("data.txt",'r')
# print(file2.read(10))
print(file2.readline())
file2.close()

# appending mode
file3 = open("data.txt",'a')
file3.write("\n baris ini dibuat dengan mode append")
file3.close()
