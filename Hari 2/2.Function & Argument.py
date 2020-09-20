# fungsi dengan argumen sederhana
def mahasiswa(nama):
    if nama == "Hafid":
        print("Mahasiswa Teladan")
    elif nama == "Lukman":
        print("Mahasiswa Nakal")
    print("mahasiswa ini bernama", nama)

# mahasiswa("Lukman")

# fungsi dengan menggunakan keywords arguments
def dosen(nama,makul):
    print("dosen ini bernama ",nama)
    print("mengajar makul ",makul)

dosen(makul="senjutsu",nama="naruto") # contoh benar
# dosen("senjutsu","naruto") # contoh salah

# fungsi dengan menggunakan default arguments
def satpam(nama,shift="pagi",galak="tidak"):
    print("dosen ini bernama:", nama)
    print("shift nya:", shift)
    print("galak?", galak)

satpam("Madara")
print(100*"*")
satpam("Paijo",shift="malam")
print(100*"*")
satpam("Asep",galak="Sangat")

