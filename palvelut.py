import random

class Asiakas:
    """Luokka asettaa asiakkaalle numeron, nimen, iän ja luo numeron.
    Julkiset methodit
        set_nimi()
        set_ika()
        get_nimi()
        get_ika()
        get_asiakasnumero()
    """
    def __init__(self, nimi, ika):
        """Konstruktorissa annetaan muuttujat, jotka peritään myöhemmin.
        :ivar asiakasnumero: asiakkaan puhelin numero
        :type asiakasnumero: int[]
        :ivar nimi: asiakkaan nimi
        :type nimi: str
        :ivar ika: asiakkaan ikä
        :type ika: int
        """
        self.__asiakasnumero = self.__luo_nro()
        self.__nimi = nimi
        self.__ika = ika
        
    def __luo_nro(self):
        """Satunnaisesti arvoo asiakkaan puhelinnumeron.
        :ivar numero: lista johon pistetään arvottu puhelinnumero
        :type numero: int[]
        """
        numero = []
        numero.append(random.randint(0, 99))
        numero.append(random.randint(0, 999))
        numero.append(random.randint(0, 999))
        return numero

    def set_nimi(self, nimi):
        """ Jos nimeä ei annettu, nostetaan virhe, jossa ilmoitetaan nimen puuttumisesta
        :param nimi: asiakkaan nimi
        :type nimi: str
        """
        if bool(nimi):
            self.nimi = nimi
        else:
            raise ValueError('Uusi nimi on annettava.')

    def set_ika(self, ika):
        """Jos type on int, sijoitetaan ikä, muutoin nostetaan virhe
        :param ika: asiakkaan ikä
        :type ika: int
        """
        if type(ika) is int:
            self.ika = ika
        else:
            raise ValueError('Virhe! Anna ika uudestaan.')

    def get_nimi(self):
        """Palautetaan __nimi
        """
        return self.__nimi

    def get_ika(self):
        """Palautetaan __ika
        """
        return self.__ika
    
    def get_asiakasnumero(self):
        """Palautetaan asiakasnumero
        """
        return f'{self.__asiakasnumero[0]:02}-{self.__asiakasnumero[1]:03}-{self.__asiakasnumero[2]:03}'

class Palvelu():
    """Luokalla hallitaan asiakaslistaa.
    Julkiset methodit
        lisaa_asiakas()
        poista_asiakas()
        get_tuotenimi()
        tulosta_asiakkaat()
    """
    def __init__(self, tuotenimi):
        """Konstruktoriin pistetään lista, jota käytetään muissa määritelmissä.
        :ivar __asiakkaat: Kaikki asiakkaiden tiedot tänne.
        :type __asiakkaat: list
        :ivar tuotenimi: Pistetään tuotenimi tännne.
        :type tuotenimi: str
        """
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def lisaa_asiakas(self, Asiakas):
        """Liittää nimen ja iän asiakaslistaan. Jos huomataan, että se on virheellinen siitä huomautetaan
        """
        if bool(Asiakas):
            self.__asiakkaat.append(Asiakas)
        else:
            raise ValueError('Asiakas on annettava')
        
    def poista_asiakas(self, Asiakas):
        """Poistetaan kutsunnassa asiakkaan nimi ja ikä. Jos asiakasta ei ole, ohitetaan virhe
        """
        try:
            self.__asiakkaat.remove(Asiakas)
        except:
            pass

    def _luo_asiakasrivi(self, Asiakas):
        """Palauttaa kutsunnasta asiakkaan nimi, asiakasnumero ja ikä"""
        return f'{Asiakas.get_nimi()}({Asiakas.get_asiakasnumero()}) on {Asiakas.get_ika()}-vuotias.'

    def tulosta_asiakkaat(self):
        """Tulostaa lopulta asiakkaan tiedot.
        """
        print("Tuotteen " + self.tuotenimi + " asiakkaat ovat")
        for asiakas in self.__asiakkaat:
            print(self._luo_asiakasrivi(asiakas))
        print()

class ParempiPalvelu(Palvelu):
    """Luokassa käsitellään tuotenimeä ja sen etuja.
    Julkiset metodit
        listaa_etu()
        poista_etu()
        tulosta_edut()
    """
    def __init__(self,tuotenimi):
        """Konstruktorissa peritään tuotenimi Palvelu luokalta
        :ivat __edut: Tuotenimen edut
        :type __edut: str[]
        """
        super().__init__(tuotenimi)
        self.__edut = []

    def lisaa_etu(self, etu):
        """Liitetään kutsunnassa pistetty etu listaan
        """
        self.__edut.append(etu)

    def poista_etu(self, etu):
        """Poistetaan kutsunnassa pistettu etu listasta. Jos ei ole olemassa, virhe ohitetaan
        """
        try:
            self.__edut.remove(etu)
        except:
            pass

    def tulosta_edut(self):
        """Lopulta tulostaa tuotenimi ja sen edut kutsunnassa
        """
        print("Tuotteeen " + self.tuotenimi + " edut ovat:")
        for etu in self.__edut:
            print(f'{etu}')
