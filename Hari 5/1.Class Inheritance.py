class Ojek():

    def __init__(self, nama, transmisi,daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id(self):
        print('nama:', self.nama,'\nmotor:', self.transmisi,'\ndaerah:',self.daerah)

class Gojek(Ojek):

    def cek_id(self):
        print('cek app gojek')

ojek1 = Ojek('mario','manual','bandung')
ojek2 = Gojek('saruto','automatic','bandung')

ojek1.cek_id()
ojek2.cek_id()