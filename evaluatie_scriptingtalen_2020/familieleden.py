def merge_two_dicts(a, b) -> dict:
    full = a.copy()  # start with x's keys and values
    full.update(b)  # modifies z with y's keys and values & returns None
    return full


def familieleden(plaats: str) -> dict:
    dict_of_family = {}
    file = open(plaats, "r")
    tekst = file.read()
    tekst = tekst.split("\n")
    # print(tekst)
    for line in tekst[:-1]:
        gezin = line.split(' ')
        dict_of_family[gezin[0]] = merge_two_dicts(dict_of_family.get(gezin[0], {}), {'kinderen': set(gezin[2:])})
        dict_of_family[gezin[1]] = merge_two_dicts(dict_of_family.get(gezin[1], {}), {'kinderen': set(gezin[2:])})
        for kind in gezin[2:]:
            dict_of_family[kind] = merge_two_dicts(dict_of_family.get(kind, {}), {'moeder': gezin[0]})
            dict_of_family[kind] = merge_two_dicts(dict_of_family.get(kind, {}), {'vader': gezin[1]})
    return dict_of_family


def get_ouder(benaming, relaties) -> str:
    if benaming == 'far':
        huidigpersoon = relaties.get('vader', None)
    else:
        huidigpersoon = relaties.get('moeder', None)
    return huidigpersoon


def voorouder(naam_familielid: str, zweedse_omschrijving: str, relaties: dict) -> str:
    huidigpersoon = naam_familielid
    benamingen = [zweedse_omschrijving[i:i + 3] for i in range(0, len(zweedse_omschrijving), 3)]
    for benaming in benamingen:
        dictvanhuidigpersoon = relaties.get(huidigpersoon)
        huidigpersoon = get_ouder(benaming, dictvanhuidigpersoon)
        assert huidigpersoon, "onbekende voorouder"
    return huidigpersoon


def nakomelingen(naam_familielid: str, n: int, relaties: dict) -> dict:
    # stel een dict op die alle nakomelingen tot de n-de generatie bevat
    # bepaal met een forloop welke benamingen er allemaal zijn:
    #     eerst kijk je naar de kinderen_A van die persoon en bepaal adhv hun dict hoe ze die persoon noemen
    #         dan kijk je naar de kinderen_B van die kinderen_A, terwijl je per kind_B het voorzetsel dat kind_A
    #         gebruikte blijft behouden

    #           en dit verder tot je aan de n-de generatie bent
    # zet deze in een dict met als sleutel de naam en als waarde de persoon die deze naam gebruikt
    pass