from Animal import Animal

class Karnivora(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, hewan_berkaki, habitat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.hewan_berkaki = hewan_berkaki
        self.habitat = habitat

    def info_karnivora(self):
        super().info_animal(),
        print("Hewan berkaki \t\t\t :" , self.hewan_berkaki,
              "\nHabitat \t\t\t :" , self.habitat)
        
karnivora = Karnivora("Singa", "rusa" , "darat", "melahirkan", "empat", "hutan")
karnivora.info_karnivora()
print("======================================================")
karnivora = Karnivora("Hiu", "ikan lain", "air asin", "bertelur beranak", "tidak ada", "perairan asin")
karnivora.info_karnivora()