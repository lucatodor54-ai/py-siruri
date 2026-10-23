from siruri2 import (
    ascunde_cardul,
    prezentare,
    cel_mai_mare_numar,
    analiza_note,
    analiza_vanzari
)
if __name__ == "__main__":
  vanzari = {
    "Laptop": 45,
    "Telefon": 2344,
    "Tableta": 1,
    "Monitor": 900,
    "Casti": 600,
    "Tastatura": 32424
  }
  print(analiza_vanzari(vanzari))


