
def prezentare(nume: str, varsta: int) -> str:
    nume=nume[0].upper()+nume[1:].lower()
    return f"{nume} are {varsta} ani"

def ascunde_cardul(numar_card: str) -> str:
    return "*" * (len(numar_card)-4) + numar_card[-4:]

def cuvinte_care_incep_cu(text: str, litera: str) -> int:
    contor = 0
    for cuvant in text.split():
        if cuvant[0].lower() == litera.lower():
            contor += 1
    return contor

def numar_telefon(numar: str) -> str:
    return "*" * (len(numar)-3)+numar[-3:]

def ascunde_codul(numar_cod: str)-> str:
    return numar_cod[:2] + "*" * (len(numar_cod)-2)

def ascunde_mijlocul(cod: str) -> str:
    return cod[:2] + "*" * (len(cod) - 4) + cod[-2:]

def ascunde_username(username: str) -> str:
    return username[:3] + "*" * (len(username)-3)

def sterge_marginile(numar: str) -> str:
    return numar[1:-1]

def sterge_marginile2(numar: str) -> str:
    return numar[2:-2]

def cuvinte_care_se_termina_cu(text:str, litera: str) -> int:
    contor = 0
    for cuvant in text.split():
        if cuvant[-1].lower() == litera.lower():
            contor += 1
    return contor

def cuvinte_cu_litera(text: str, litera: str) -> int:
    contor = 0
    for cuvant in text.split():
        if litera.lower() in cuvant.lower():
            contor += 1
    return contor

def numara_cuvinte_lungi(text: str, lungime: int) -> int:
    contor = 0
    for cuvant in text.split():
        if len(cuvant) > lungime:
            contor += 1
    return contor

def cel_mai_lung_cuvant(text:str)-> str:
    cel_mai_lung = ""
    for cuvant in text.split():
        if len(cuvant) > len(cel_mai_lung):
            cel_mai_lung = cuvant
    return cel_mai_lung

def cel_mai_scurt_cuvant(text:str)-> str:
    cuvinte =  text.split()
    cel_mai_scurt = cuvinte[0]
    for cuvant in cuvinte:
        if len(cuvant) < len(cel_mai_scurt):
            cel_mai_scurt = cuvant
    return cel_mai_scurt

def cel_mai_lung_cuvant_cu_litera(text:str, litera:str)-> str:
    cel_mai_lung = ""
    for cuvant in text.split():
        if litera.lower() in cuvant.lower() and len(cuvant) > len(cel_mai_lung):
            cel_mai_lung = cuvant
    return cel_mai_lung

def numar_total_litere(text: str) -> int:
    total = 0
    for cuvant in text.split():
        total += len(cuvant)
    return total

def numar_total_litere_cuvinte_lungi(text: str) -> int:
    total = 0
    for cuvant in text.split():
        if len(cuvant) > 4:
            total += len(cuvant)
    return total

def formatare_nume(text: str) -> str:
    rezultat = ""
    for cuvant in text.split():
        rezultat += cuvant.capitalize() + " "
    return rezultat.strip()

def litera_din_mijloc(text: str) -> str:
    mijloc = len(text)//2
    if (len(text) % 2) != 0:
        return text[mijloc]
    else:
        return text[mijloc-1:mijloc+1]

def prima_jumatate(text:str) -> str:
    mijloc = len(text)//2
    return text[:mijloc]

def a_doua_jumatate(text:str) -> str:
    mijloc = len(text)//2
    return text[mijloc:]

def dupa_mijloc(text: str) -> str:
    mijloc = len(text) // 2
    if (len(text) % 2) != 0:
        return text[mijloc+1:]
    else:
        return text[mijloc:]

def suma_din_text(text: str) -> int:
    if text == "":
        return 0
    total = 0
    for bucata in text.split(","):
        total += int(bucata)
    return total

def numere_mai_mari_de_10(text:str) -> int:
    if text == "":
        return 0
    contor = 0
    for bucata in text.split(","):
        bucata = int(bucata)
        if bucata > 10:
            contor += 1
    return contor


def suma_numerelor_pare(text: str) -> int:
    if text == "":
        return 0
    total = 0
    for bucata in text.split(","):
        bucata = int(bucata)
        if bucata % 2 == 0:
            total += bucata
    return total

def cel_mai_mare_numar(text: str) -> int:
    if text == "":
        return 0
    maxim = 0
    for bucata in text.split(","):
        bucata = int(bucata)
        if bucata > maxim:
            maxim = bucata
    return maxim

def cel_mai_mic_numar(text: str) -> int:
    if text == "":
        return 0
    bucati = text.split(",")
    minim = int(bucati[0])
    for bucata in bucati:
        bucata = int(bucata)
        if bucata < minim:
            minim = bucata
    return minim

def parola_buna(parola: str)-> bool:
    if len(parola) < 8:
        return False
    are_cifra = False
    for litera in parola:
        if litera in "0123456789":
            are_cifra = True
    if are_cifra == True and parola!=parola.lower():
        return True
    else:
        return False

def username_valid(username: str) -> bool:
    if len(username) < 6:
        return False

    are_cifra = False
    are_litera = False

    for litera in username:
        if litera in "0123456789":
            are_cifra = True

        if litera.lower() in "abcdefghijklmnopqrstuvwxyz":
            are_litera = True

    if are_cifra == True and are_litera == True and " " not in username:
        return True
    else:
        return False

def email_valid(email:str)->bool:
    if len(email)<8:
        return False
    are_cifra = False
    are_arond = False
    are_punct = False

    for litera in email:
        if litera in "0123456789":
            are_cifra = True
        if litera in "@":
            are_arond = True
        if litera in ".":
            are_punct = True


    if are_cifra == True and are_punct == True and are_arond == True and " " not in email:
        return True
    else:
        return False

##Codul este valid dacă:
##- are exact 10 caractere
##- conține cel puțin 2 cifre
##- conține cel puțin o literă mare
##- conține cel puțin o literă mică
##- nu conține spații

def cod_acces_valid(cod: str)->bool:
    if len(cod) != 10:
        return False
    contor = 0
    litera_mare = False
    litera_mica = False

    for litera in cod:
        if litera in "0123456789":
            contor += 1
        if litera in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            litera_mare = True
        if litera in "abcdefghijklmnopqrstuvwxyz":
            litera_mica = True
    if contor >= 2 and litera_mare == True and litera_mica == True and " " not in cod:
        return True
    else:
        return False

tranzactii = [450, 1200, 850, 2300, 1750, 600, 3100, 950, 2800]
def analiza_tranzactii(tranzactii):
    suma = 0
    contor = 0
    suma_mari = 0

    for tranzactie in tranzactii:
        suma += tranzactie
        if tranzactie >= 1500:
            contor += 1
            suma_mari += tranzactie
    if contor != 0:
        media = suma_mari / contor
    else:
        media = 0
    return suma, contor, suma_mari, media

salarii = [3200, 4500, 2800, 6000, 5100, 3500, 7200, 4100]
def analiza_salarii(salarii):
    contor = 0
    suma_mari = 0
    maxim = salarii[0]
    minim = salarii[0]
    for salar in salarii:
        if salar >= 4500:
            contor += 1
            suma_mari += salar
        if salar > maxim:
            maxim = salar
        if salar < minim:
            minim = salar
    return maxim, minim, contor, suma_mari

vanzari = {
    "Laptop": 4500,
    "Telefon": 2800,
    "Tableta": 1500,
    "Monitor": 900,
    "Casti": 600,
    "Tastatura": 1200
}

def analiza_vanzari(vanzari):
    contor = 0
    suma_mari = 0
    maxim = 0
    produs_maxim = ""
    for produs, valoare in vanzari.items():
        if valoare >= 1500:
            contor += 1
            suma_mari += valoare
        if valoare > maxim:
            maxim = valoare
            produs_maxim = produs
    media = suma_mari / contor
    media = round(media, 2)
    return produs_maxim, contor, suma_mari, media

note = {
    "Andrei": 7,
    "Maria": 10,
    "Alex": 6,
    "Ioana": 9,
    "Mihai": 8,
    "Elena": 5,
    "David": 9,
    "Sandra": 10
}
def analiza_note(note):
    contor = 0
    suma = 0
    cea_mai_mica = list(note.values())[0]
    student_minim = ""
    for student, nota in note.items():
        suma += nota
        if nota >= 8:
            contor += 1
        if nota < cea_mai_mica:
            cea_mai_mica = nota
            student_minim = student
    media = suma / len(note)
    media = round(media, 2)
    return student_minim,cea_mai_mica, contor, media

cheltuieli = {
    "Mancare": 1850,
    "Transport": 650,
    "Haine": 1200,
    "Facturi": 950,
    "Divertisment": 500,
    "Facultate": 1400
}
def analiza_cheltuieli(cheltuieli):
    contor = 0
    suma = 0
    suma_mari = 0
    cea_mai_mare = list(cheltuieli.values())[0]
    categoria_maxima = list(cheltuieli.keys())[0]
    for categorie, valoare in cheltuieli.items():
        suma += valoare
        if valoare >= 1000:
            contor +=1
            suma_mari += valoare
        if valoare > cea_mai_mare:
            cea_mai_mare = valoare
            categoria_maxima = categorie
    media = suma / len(cheltuieli)
    media = round(media, 2)
    return categoria_maxima, cea_mai_mare, contor, suma_mari, media

vanzari = {
    "Alba": [1200, 1800, 900, 2500],
    "Cluj": [2200, 3100, 1500, 2800],
    "Sibiu": [800, 1100, 700, 1400]
}

def analiza_vanzari1(vanzari):
    contor = 0
    suma = 0
    maxim = 0
    nume_maxim = ""
    for magazin, lista in vanzari.items():
        total_magazin = 0
        for vanzare in lista:
            suma += vanzare
            total_magazin += vanzare
            if vanzare >= 2000:
                contor += 1

        if total_magazin > maxim:
            maxim = total_magazin
            nume_maxim = magazin

    return nume_maxim, maxim, suma, contor

produs = ("Laptop", 4500, 3)
def analiza_produs(produs):
    nume, pret, cantitate = produs
    valoarea_totala = pret * cantitate
    return nume,pret,cantitate, valoarea_totala

produse = [
    ("Laptop", 4500, 2),
    ("Telefon", 2800, 3),
    ("Monitor", 1200, 4),
    ("Tastatura", 500, 5)
]
def analiza_prod(produse):
    contor = 0
    suma_totala = 0
    produs_max = 0
    numele_produsului_max = ""
    for nume, pret, cantitate in produse:
        suma_totala += pret * cantitate
        if pret >= 2000:
            contor += 1
        if pret > produs_max:
            produs_max = pret
            numele_produsului_max = nume
    return numele_produsului_max, produs_max, suma_totala, contor

def fara_dubluri(text: str) -> str:
    if text == "":
        return ""
    rezultat = text[0]
    for i in range(1, len(text)):
        if text[i] != text[i - 1]:
            rezultat += text[i]
    return rezultat

def fara_cifre_dublate(text: str) -> str:
    if text =="":
        return ""
    rezultat = text[0]
    for i in range(1, len(text)):
        if text[i] != text[i-1]:
            rezultat += text[i]
    return rezultat

def numara_grupuri(text:str)->int:
    if text == "":
        return 0
    contor = 1
    for i in range(1, len(text)):
        if text[i] != text[i-1]:
            contor += 1
    return contor

def cea_mai_lunga_serie(text:str)->int:
    if text == "":
        return 0
    contor = 1
    maxim = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            contor += 1
        else:
            contor = 1
        if contor > maxim:
            maxim = contor
    return maxim

def cea_mai_lunga_serie_pare(text: str) -> int:
    if text == "":
        return 0
    contor = 0
    maxim = 0
    for i in range(len(text)):
        if int(text[i]) % 2 == 0:
            contor += 1
        else:
            contor = 0
        if contor > maxim:
            maxim = contor
    return maxim

def cea_mai_lunga_serie_litera(text: str) -> tuple:
    if text == "":
        return "", 0
    contor = 1
    maxim = 1
    litera_max = text[0]
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            contor += 1
        else:
            contor = 1
        if contor > maxim:
            maxim = contor
            litera_max = text[i]
    return litera_max, maxim

salarii = [2800, 4500, 3200, 6000, 7500, 3900]
salarii_mari = [salar for salar in salarii if salar >= 4500]

preturi = [100, 200, 350, 500]
preturi_duble = [pret * 2 for pret  in preturi]

numere = [2, 4, 6, 8, 10]
numere_la_patrat = [numar ** 2 for numar in numere]

numere = [1, 2, 3, 4, 5, 6, 7, 8]
numere_pare = [numar for numar in numere if numar % 2 == 0]

numere = [1, 2, 3, 4, 5, 6, 7, 8]
numere_par_la_patrat = [numar ** 2 for numar in numere if numar % 2 ==0]

def este_anagrama(a: str, b: str)->bool:
    a = a.lower().replace(" ", "")
    b = b.lower().replace(" ", "")
    return sorted(a) == sorted(b)

def aceleasi_vocale(a: str, b: str)->bool:
    a = a.lower().replace(" ", "")
    b = b.lower().replace(" ", "")
    for vocala in "aeiou":
        if a.count(vocala) != b.count(vocala):
            return False
    return True

















