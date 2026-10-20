from siruri2 import (
  prezentare,
  ascunde_cardul,
  cuvinte_care_incep_cu,
  numar_telefon,
  ascunde_codul,
  ascunde_mijlocul,
  ascunde_username,
  sterge_marginile,
  sterge_marginile2,
  cuvinte_care_se_termina_cu,
  cuvinte_cu_litera,
  numara_cuvinte_lungi,
  cel_mai_lung_cuvant,
  cel_mai_scurt_cuvant,
  cel_mai_lung_cuvant_cu_litera,
  numar_total_litere,
  numar_total_litere_cuvinte_lungi,
  formatare_nume,
  litera_din_mijloc,
  suma_din_text,
  parola_buna,
  email_valid,
  cod_acces_valid,
  analiza_tranzactii,
  analiza_salarii,
  analiza_vanzari,
  analiza_note,
  analiza_cheltuieli,
  analiza_vanzari1,
  analiza_produs,
  analiza_prod
)
if __name__ == "__main__":
  produse = [
    ("Laptop", 4500, 2),
    ("Telefon", 2800, 3),
    ("Monitor", 1200, 4),
    ("Tastatura", 500, 5)
  ]

  rezultat = analiza_prod(produse)
  print(rezultat)


