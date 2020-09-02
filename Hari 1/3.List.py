Data = [4,7,3,10,12,33,99,34]

# mengakses list
SubData = Data[3]
SubData1 = Data[-3]

# memotong list
SubData3 = Data[2:4]
SubData4 = Data[-4:]

# menambah list
Data2 = [100,300,400,500,700]
DataConc = Data + Data2

# merubah content list
Data[5] = 15

# Mengcopy list ke variabel baru
a = Data[:]
a[1] = 20
# print(a)

# merubah content list dengan metode slicing
Data[3:5] = [18,22]
# print(Data)

# list dalam list
x = [Data,Data2]
# print(x)

# mengakses list dalam multidimensional list
y = x[1][3]
# print(y)

# methods list
# append (menambah data)
Data.append(10)
print(Data)
# function
panjang_list = len(Data)
print("panjang:",panjang_list)

