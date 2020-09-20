# list = [1,2,3,4]
# tuple = (1,2,3,4)
# set = {1,2,3,4}
#
# print(type(list))
# print(type(tuple))
# print(type(set))

# dictionary
member1 = {
            "ID":197,
            "Nama":"M Hafid Masruri",
            "Pekerjaan":"Mahasiswa",
            "Status Member": "Gold"
          }

member2 = {
            "ID":199,
            "Nama":"Deddy Gunawan",
            "Pekerjaan":"Mahasiswa",
            "Status Member": "Silver"
          }


memberList = {197:member1,199:member2}
print(memberList[197])

# print(member1["Nama"])
# print(member1.keys())
# print(member1.values())
# print(member1.items())