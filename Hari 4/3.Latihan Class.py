class shinobi():


    def __init__(self, kecer, kekua, kecep):
        self.kecerdasan = kecer
        self.kekuatan = kekua
        self.kecepatan = kecep

    def Uchiha(self,nama):
        print("=====", nama, "=====")
        print('Kecerdasan = ', self.kecerdasan)
        print('Kekuatan = ', self.kekuatan)
        print('Kecepatan = ', self.kecepatan)

        total_madara = self.kecerdasan + self.kekuatan + self.kecepatan / 5
        print("Total = ",total_madara)

    def Namikaze(self,nama):
        print("=====", nama, "=====")
        print('Kecerdasan = ', self.kecerdasan)
        print('Kekuatan = ', self.kekuatan)
        print('Kecepatan = ', self.kecepatan)

        total_minato = self.kecerdasan + self.kekuatan + self.kecepatan / 5
        print("Total = ",total_minato)


Madara = shinobi(85,95,85)
Madara.Uchiha("Uchiha Madara")

Minato = shinobi(95,80,90)
Minato.Namikaze("Minato Namikaze")



