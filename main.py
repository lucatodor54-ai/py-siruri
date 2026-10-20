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
  analiza_vanzari
)
if __name__ == "__main__":
  vanzari = {
    "Laptop": 4500,
    "Telefon": 2800,
    "Tableta": 1500,
    "Monitor": 900,
    "Casti": 600,
    "Tastatura": 1200
  }

  rezultat = analiza_vanzari(vanzari)
  print(rezultat)


