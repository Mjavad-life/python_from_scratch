class Restaurant :
    def __init__(self , name , makan ) :
        self.name = name 
        self.makan = makan 
    def rest_tozih(self) :
        print(f"{self.name} esm ma , va {self.makan} mahale mast")

class Ghif :
    def __init__(self ):
        self.shekl = ['hozloli' , 'varoneh' , 'tah gerd']

    def chap(self) :
        print(self.shekl)   

class Bastani(Restaurant) :
    def __init__(self, name, makan):
        super().__init__(name, makan)
        self.mazeha=['shokol','sonati','shatot']
        self.ghif=Ghif()

    def namayesh_mazeha(self) :
        print(self.mazeha)

bastanie_man=Bastani('sonati' , 'janat abad')
bastanie_man.namayesh_mazeha()
bastanie_man.rest_tozih()
print(bastanie_man.ghif.shekl)