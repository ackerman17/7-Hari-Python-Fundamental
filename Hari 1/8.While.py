# angka = 0
#
# while angka < 5: #iterasi
#     print('nilai angka adalah :', angka)
#     angka = angka +1
#
# print('diluar while')

# start = True
# angka = 0
#
# while start:
#     print("ini dalam while")
#     if angka is 10:
#         start = False
#         print("oke angka 100 ditemukan")
#     angka +=1


angka = 0
while angka < 10: #iterasi

    if angka == 5:
    #     break
        angka+=1
        continue

    print('nilai angka adalah :', angka)
    angka = angka+1
else:
    print('nilai angka diakhir while adalah ', angka)

print('diluar while')