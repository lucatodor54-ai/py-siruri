def prezentare(nume: str, varsta: int) -> str:
    nume=nume[0].upper()+nume[1:].lower()
    return f"{nume} are {varsta}"

def ascunde_cardul(numar_card: str) -> str:
    return "*" * (len(numar_card)-4) + numar_card[:-4]

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









