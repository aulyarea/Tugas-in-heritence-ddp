from Animal import Animal

class Mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, habitat, jenis_hewan):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.jenis_hewan = jenis_hewan

    def info_mamalia(self) :
        super().info_animal(),
        print("habitat \t\t\t : ", self.habitat,
              "\nJenis Hewan \t\t\t : ", self.jenis_hewan)
        
mamalia = Mamalia("Beruang kutub", "ikan" , "darat", "melahirkan" , "kutub utara" , "karnivora")
mamalia.info_mamalia()
print("=====================================================================")
mamalia = Mamalia("Lumba-lumba", "ikan", "air laut dan air tawar", "melahirkan", "perairan", "karnivora")
mamalia.info_mamalia()

