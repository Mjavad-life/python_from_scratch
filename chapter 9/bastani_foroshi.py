from restoran import Restaurant
from ghifha import Ghif
class Bastani(Restaurant) :
    def __init__(self, name, makan):
        super().__init__(name, makan)
        self.mazeha=['shokol','sonati','shatot']
        self.ghif=Ghif()

    def namayesh_mazeha(self) :
        print(self.mazeha)