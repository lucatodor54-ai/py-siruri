def utilizator_din_email(email: str) -> str:
    pozitie = email.find("@")
    if pozitie == -1:
        return ""
    return email[:pozitie] ## email[:4]
###  "
## pt: Ana are 3 mere si 4 pere
## litera  liteara.isdigit() suma
##  A         nu             -
##  n         nu             -
##  a         nu             -
##            nu             -
##  a         nu             -
##  r         nu             -
##  e         nu             -
##            nu             -
##  3         da             3
##            nu             -
##  m         nu             -
##  e         nu             -
##  r         nu             -
##  e         nu             -
##            nu             -
##  s         nu             -
##  i         nu             -
##            nu             -
##  4         da             7
##  p         nu             -
##  e         nu             -
##  r         nu             -
##  e         nu             -
def suma_cifrelor_din_text(text: str)->int:
    suma = 0
    for litera in text:
        if litera.isdigit():
            suma += int(litera)
    return suma
### ("1.2.2026").split(".")=["21","22,"2026"]

def valideaza_data(data:str)->bool:
     bucati = data.split(".")
     if len(bucati)!=3 :
         return False
     zi,luna,anul=bucati

     if not (zi.isdigit() and anul.isdigit() and luna.isdigit()):
         return False

     zi,luna,anul=int(zi),int(luna),int(anul)

     if not (1<=luna<=12):
         return False

     zile_in_luna = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

     if not (1<=zi<=zile_in_luna[luna-1]):
         return False

     return True


def data_iso(data: str)->str:
    if not (  valideaza_data(data)):
        return "Data invalida"
    bucati=data.split(".")
    zi=bucati[0]
    luna=bucati[1]
    anul=bucati[2]
    if len((zi)) == 1:
        zi="0"+zi
    if len((luna)) == 1:
        luna = "0" + luna

    return f"{zi}-{luna}-{anul}"

def ziua_cea_mai_calda(temperaturi: str)-> int:
    zile = temperaturi.split(",")###[21,25,19]
    maxim = int(zile[0])
    contor = 0
    pozitie = 0
    for zi in zile:
        temperatura=int(zi)
        if temperatura > maxim:
            maxim = temperatura
            pozitie = contor
        contor += 1
    return pozitie
##### "paine:3,lapte:7,ou:1".split(,)=>["paine:3","lapte:7","ou:1"]
#### "paine:3".split(":")=>["paine" ,"3"]
def cel_mai_ieftin (produse: str)->str:
    bucati=produse.split(",")
    pret_minim=1000
    nume_produs_minim=""
    for prod in bucati:
        produs=prod.split(":")
        pret=int(produs[1])
        if pret<pret_minim :
           pret_minim=pret
           nume_produs_minim=produs[0]
    return nume_produs_minim

def caractere_diferite(text: str)->int:
    text = text.lower()
    diferite = []
    for caracter in text:
        if caracter not in diferite:
            diferite.append(caracter)
    return len(diferite)

def numara_aparitii(text:str, bucata: str)->int:
    contor = 0
    for i in range(len(text)-len(bucata)+1):
        if text[i:i + len(bucata)] == bucata:
            contor += 1
    return contor

def suma_numerelor_din_text(text:str)->int:
    suma = 0
    numar = ""
    for caracter in text:
        if caracter in "0123456789":
            numar += caracter
        else:
            if numar != "":
                suma+=int(numar)
                numar = ""
    if numar != "":
        suma += int(numar)
    return suma







