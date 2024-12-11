from Animal import Animal


# setiap class child itu memeliki 2 properti dan method
class Amphibi(Animal) :
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas) :
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi(self) :
        super().info_animal(),
        print("jenis Air \t\t\t : ", self.jenis_air,
              "\nBernapas \t\t\t : ", self.bernapas)
        
amphibi = Amphibi("katak", "serangga" , "dua alam", "bertelur" , "air tawar", "kulit dan Paru-paru")
amphibi.info_amphibi()
print("===============================================")
amphibi = Amphibi("salamender", "ikan" , "dua alam" , "nertelur beranak" , "air tawar" , "kulit dan paru-paru") 
amphibi.info_amphibi()
