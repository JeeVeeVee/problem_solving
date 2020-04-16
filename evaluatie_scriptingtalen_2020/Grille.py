class Grille:
    def __init__(self, aantal_rijen: int, collectie):
        self.dimensie = aantal_rijen
        self.openingen = set(collectie)
        self.matrix = [[None for _ in range(self.dimensie)] for __ in range(self.dimensie)]

    def roteer(self, wijzerzin=True):
        nieuwe_openingen = set()
        if wijzerzin:
            for element in self.openingen:
                a = element[1]
                b = self.dimensie - element[0] - 1
                nieuwe_openingen.add((a, b))
        else:
            for element in self.openingen:
                a = self.dimensie - element[1] - 1
                b = element[0]
                nieuwe_openingen.add((a, b))
        self.openingen = nieuwe_openingen
        return self

    def decodeer(self, plaats):
        bestand = open(plaats, 'r')
        tekst = bestand.read().split("\n")
        bericht = ""
        for i in range(self.dimensie):
            for j in range(self.dimensie):
                if (i, j) in self.openingen:
                    bericht += tekst[i][j]

        return bericht

    def __repr__(self):
        full = ""
        for i in range(self.dimensie):
            string = ""
            for j in range(self.dimensie):
                if (i, j) in self.openingen:
                    string += "0"
                else:
                    string += "#"
            full += string + "\n"
        return full.rstrip("\n")

    def __str__(self):
        full = ""
        for i in range(self.dimensie):
            string = ""
            for j in range(self.dimensie):
                if (i, j) in self.openingen:
                    string += "O"
                else:
                    string += "#"
            full += string + "\n"
        return full.rstrip("\n")

    def __eq__(self, other):
        # turnable gebruiken want anders wordt other aangepast en niet teruggezet zonder dat we dat willen
        turnable = Grille(other.dimensie, other.openingen)
        if self.dimensie != turnable.dimensie:
            return False
        if self.openingen == turnable.openingen:
            return True
        for i in range(3):
            turnable.roteer()
            if self.openingen == turnable.openingen:
                return True
        return False

    def __add__(self, other):
        assert self.dimensie == other.dimensie, "ongeldige bewerking"
        return Grille(self.dimensie, [y for y in self.openingen if y in other.openingen])




