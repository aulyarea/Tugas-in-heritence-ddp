# buat class animal sebagai parent class. class animal mempunayi properti 4 properti
#  (name, makanan, hidup, berkembang biak)

class Animal:
    def __init__ (self, name, makanan, hidup, berkembang_biak): 
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info_animal (self):
        print("Nama Hewan \t\t\t : ", self.name,
              "\nMakanan \t\t\t : " , self.makanan,
              "\nHidup \t\t\t\t : ", self.hidup,
              "\nBerkembang Biak \t\t : ", self.berkembang_biak )

# hewan = Animal ("Kucing", "Daging", "darat", "beranak")
# hewan.info_animal()

# class child
# buat 3 objek dari class animal dengan properti yang berbeda-beda