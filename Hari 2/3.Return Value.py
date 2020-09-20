# fungsi dengan return value
def kuadrat(argumen):
    total = argumen**2
    print('nilai kuadrat dari', argumen, 'adalah', total)
    return total

print(kuadrat(4))

print(100*"*")

# fungsi dengan return value dan multiple argumen
def tambah(argumen1,argumen2):
    total = argumen1 + argumen2
    print(argumen1 , '+', argumen2, "=", total)
    return  total

def kali(argumen1,argumen2):
    total = argumen1 * argumen2
    print(argumen1 , '*', argumen2, "=", total)
    return  total

# a = tambah(3,4)
# b = kali(3,a)
simple = kali(5,tambah(3,4))


