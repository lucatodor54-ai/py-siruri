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
  analiza_note
)
if __name__ == "__main__":
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

  rezultat = analiza_note(note)
  print(rezultat)


