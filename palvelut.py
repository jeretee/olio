import random

class Asiakas:
    def __luo_nro(self):
        """Muodostaa satunnaisen asiakasnumeron
        :ivar numerolista: lista jossa satunnaisesti generoitu asiakasnumero
        :type numerolista: int[]
        """
        numerolista = []
        numerolista.append(random.randint(0, 99))
        numerolista.append(random.randint(0, 999))
        numerolista.append(random.randint(0, 999))
        return numerolista

    def __init__(self, nimi, ika):
        """Konstruktori, jonka muuttujat peritÃ¤Ã¤n
        :ivar asiakasnumero: asiakkaan puhelin numero
        :type asiakasnumero: int[]
        :ivar nimi: asiakkaan nimi
        :type nimi: str
        :ivar ika: asiakkaan ikÃ¤
        :type ika: int
        """
        self.__asiakasnumero = self.__luo_nro()
        self.__nimi = (str)nimi
        self.__ika = (int)ika

        def get_nimi(self):
            return self__nimi
        def get_ika(self):
            return self.__ika
        def set_nimi(self, uusinimi):
            if uusinimi == False:
                raise ValueError:("Anna toinen nimi")
            if uusinimi == True:
                self.__nimi = uusinimi
        def set_ika(self, uusiika):
            if lisaanimi == True:
                raise ValueError:("Anna toinen ika"):
            if uusika == True:
                self.__ika = uusiika

class Palvelu:
    def __init__(self, Asiakas):
        self asiakkaat = []
    def luo_asiakasrivi(self, Asiakas)
    def lisaa_asiakas(self, Asiakas)
    def poista_asiakas(self, Asiakas)
    def tulosta_asiakkaat(self)
    





class ParempiPalvelu:
    def __init__(self):
        def __edut
    def lisaa_etu(self):
        pass
    def poista_etu(self):
        pass
    def tulosta_edut(self):
        pass
