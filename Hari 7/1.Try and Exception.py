while True:
    try:
       penyebut = int(input("masukkan angka penyebut = "))
       pembilang = int(input("masukkan angka pembilang = "))
       hasil = penyebut / pembilang
       break

    except ValueError:
        print("yang anda masukkan bukan angka")
    except ZeroDivisionError:
        print("angka pembilang yang anda masukkan adalah nol, pilih yg lain brow")

print("berhasil, hasil pembagian adalah:", hasil)