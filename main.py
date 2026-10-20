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
  analiza_salarii
)
if __name__ == "__main__":
  salarii = [3200, 4500, 2800, 6000, 5100, 3500, 7200, 4100]
  rezultat = analiza_salarii(salarii)
  print(rezultat)


