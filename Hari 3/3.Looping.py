# teknik looping

# list
nama_band = ['Payung Teduh',
             'Moshimo',
             'Flow',
             'Asian Kungfu Generation'
             ]

kumpulan_lagu = ['Akad',
        'Zona Nyaman',
        'Sign',
        'Blue Bird'
        ]

# enumerate
for i ,band in enumerate(nama_band):
    print(i,':',band)
print(100*"=")

# zip
for band,lagu in zip(nama_band,kumpulan_lagu):
    print(band,' | lagu:', lagu)

print(100*"=")

# set
playlist = {'cenat cenut','flow','blue bird'}
for lagu in sorted(playlist):
    print(lagu)


print(100*"=")
# dictonary
playlist2 = {'maherzain': 'insha allah',
             'kana boon': 'silhoutte',
             'flow': 'sign',
             'zivillia': 'pintu taubat'
             }

for i,z in playlist2.items():
    print(i,'| lagunya:',z)

for i in reversed(range(1,10,1)):
    print(i)