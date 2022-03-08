class Asiakas:
    """Luokka jossa syötetään asiakkaan tiedot
    :ivar __nimi: asiakkaan nimi
    :type __nimi: str
    :ivar __asiakasnro: asiakkaan numero
    :type __asiakasnro: int
    :ivar __ika: asiakkaan ikä
    :type __ika: int
    Julkiset metodit
        __luo_nro()
    """

    def __init__(self):
        """konstruktori"""
        self.__nimi = ""
        self.__asiakasnro = self.__luo_nro()
        self.__ika = ""

class Palvelu:
    """Palvelu luokka
    :ivar tuotenimi: tuotteen nimi
    :type tuotenimi: str
    :ivar __asiakkaat: lista asiakkasita
    :type __asiakkaat: list
    Julkiset metodit
        _luo_asiakasrivi(Asiakas)
        lisaa_asiakas(Asiakas)
        poista_asiakas(Asiakas)
        tulosta_asiakkaat()
    """

    def __init__(self):
        """konstruktori"""
        self.tuotenimi = ""
        self.__asiakkaat = asiakkaat()

class ParempiPalvelu:
    """ParempiPalvelu luokka
    :ivar edut: palvelun edut
    :type edut: str, list
    Julkiset metodit
        _lisaa_etu(str)
        _poista_etu(str)
        _tulosta_edut()
    """

    def __init__(self):
        """konstruktori"""
        self.edut = edut()
