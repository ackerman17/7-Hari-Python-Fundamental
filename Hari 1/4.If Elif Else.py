
nilai = 70

if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai < 80:
    print("nilai anda adalah B")
elif 60 <= nilai <70:
    print("nilai anda adalah C")
elif 50 <= nilai < 60:
    print("nilai anda jelek,lakukan perbaikan")
else:
    print("maaf,anda gak lulus bisa ngulang tahun depan")


print(100*"=")
print("operator logika untuk list dan string")

gorengan = ["bakwan goreng","weci anget","jemblem","tahu genjot","tempe mendoan"]
beli = "bakwan goreng"

if beli in gorengan:
    print("mhank saya mau beli",beli)
if not beli in gorengan:
    print("sorry bro gua gak jual tuh:", beli)

kata = "goreng"
if kata in beli:
    print("ada", kata)
else:
    print("tidak ada",kata)