


def parcuregere():
    #### ['A','n'...'e']
    text="Ana are mere"
    for litera in text:
        print(litera)

##### "Ana" +"are" =>  "Anaare"
#  "3" +"4"=>"34"
#  3 +"4"
def  parcurgre_index():
    text="Ana are mere"
    for poz,litera in enumerate(text):
        print("Metoda 1 :"+str(poz)+" "+litera)
        print(poz,litera)
        print("========================")

def lower_upper():
    "Ana".lower()
    "Ana".upper()
    print("Ana".lower())
    print("+")
    print("Ana".upper())
    print("========")
    print("Ana".lower()+" " + "Ana".upper())

def strip():
    "Ana".strip()
    print("Ana".strip())
    "Ana are".strip()
    print("Ana are".strip())
    print("+")

def parcurgere_lista_texte():
    cuvinte = ["Ma", "duc", "acasa", "azi", "e", "miercuri"]

    for i in range(0, len(cuvinte)):
        print(cuvinte[i])

def split():
    for cuvant in "Ana, are, mere".split(","):
        print(cuvant)

def replace():
    for cuvant in "a-b-c".replace("-", ""):
        print(cuvant)

def count():

    return "banana".count("a")


def numara_cifre():
    s="text123456789"
    contor = 0
    for caracter in s:
       if caracter.isdigit():
           contor +=1
    return contor



def numara_litere():
    l="ana are mere"
    contor = 0
    for caracter in l:
        if caracter == "a":
            contor +=1
    return contor


def cate_vocale(v):
    contor = 0
    for vocale in v:
        if vocale in "aeiou":
            contor +=1
    return contor


def cate_consoane(c):
    contor = 0
    for consoane in c:
        if consoane not in "aeiou":
            contor +=1
    return contor

