

def prima_litera(text: str) -> str:
    return text[::-1]


def ultima_litera(text: str) -> str:
    return text[-1]


def primele_trei(text: str) -> str:
    return text[:3]
    pass


def inversat(text: str) -> str:
    return text[::-1]
    pass

## pt python:
##    litera   litera in "aeiou"   contor
#         p             nu            -
#         y             nu
#         t             nu
#         h             nu
#         o             da         1
#         n             nu
def numar_vocale(text: str) -> int:
   contor = 0
   text = text.lower()
   for litera in text:
       if litera in "aeiou":
          contor += 1
   return contor



def numar_cuvinte(text: str) -> int:
     cuvinte = text.split()
     return len(cuvinte)



def initiale(nume_complet: str) -> str:
    cuvinte = nume_complet.split()
    rezultat = ""
    for cuvant in cuvinte:
        rezultat += cuvant[0]
    return rezultat
## Ana ar avea mere multe  =>["Ana" ,"ar" ,"avea","mere","multe"]

         ## cuvant   cuvant> cel_mai_lung  cel_mai_lung
         ##  ana      ana > "" da           ana
         ##  ar       ar > ana  nu          -
         ## avea      avea > ana da         avea
         ## mere      mere > avea nu        -
         ## multe     multe > avea da       multe


def cuvantul_cel_mai_lung(text: str) -> str:
    cuvinte = text.split()
    cel_mai_lung = ""
    for cuvant in cuvinte:
       if len(cuvant) > len(cel_mai_lung):
         cel_mai_lung = cuvant
    return cel_mai_lung


def este_palindrom(text: str) -> bool:
    return text[::-1] == text


def suma_cifrelor(n: int) -> int:
    suma = 0
    for cifra in str(n):
        suma += int(cifra)
    return suma
