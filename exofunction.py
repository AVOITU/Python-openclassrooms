def salaire_mensuel(salaire_annuel):
  salaire_mensuel=int(salaire_annuel)/12
  return salaire_mensuel

def salaire_hebdomadaire(salaire_mensuel):
  salaire_hebdomadaire=salaire_mensuel/4
  return salaire_hebdomadaire

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
  salaire_horaire=salaire_hebdomadaire/heures_travaillees
  return salaire_horaire

def main():
  print("saisir le salaire annuel à calculer :")
  salaire_annuel=input()
  print("saisir le nombre d'heures travaillées par semaine :")
  heures_travaillees=input()
  salaire_mensuel(salaire_annuel)
  print(salaire_mensuel)
  salaire_hebdomadaire(salaire_mensuel)
  print(salaire_hebdomadaire)
  salaire_horaire(salaire_hebdomadaire, heures_travaillees)
  print (f"votre salaire horaire est de {salaire_horaire} euros")

if __name__=="__main__":
  main()