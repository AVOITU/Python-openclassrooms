def saisie_nombres():
  while True:
    try:
      print(
        "Saisisez une série de chiffres entier séparés par des  virgules et ne mettre aucun espace, par exemple 1,2,3,4"
      )
      saisie = input()
      #crée une liste et la convertit en prévision de son utilisation dans les calculs
      nombres = [int(nombre) for nombre in saisie.split(',')]
      return nombres
    except ValueError:
      print((
        "Erreur : veuillez entrer des chiffres entiers valides avec la virgule comme séparateur"
      ))


def informations_mathématiques(nombres):
  #crée la somme, la moyenne et les nombres supérieurs grâce à des expressions génératrices et calculs
  somme = sum((nombre) for nombre in nombres)
  moyenne = somme / len(nombres)
  nombres_supérieurs = sum(1 for nombre in nombres if nombre > moyenne)
  return somme, moyenne, nombres_supérieurs


def nombres_pairs(nombres):
  #création de la boucle while selon les instructions openclassrooms pour générer le nombre de nombre de nombre pairs
  indice = 0
  nombres_pairs = 0
  while indice < len(nombres):
    if nombres[indice] % 2 == 0:
      indice = indice + 1
      nombres_pairs = nombres_pairs + 1
    else:
      indice = indice + 1
  return nombres_pairs


def main():
  #execution de la saisie et des calculs des fonctions précédentes
  nombres = saisie_nombres()
  somme, moyenne, nombres_supérieurs = informations_mathématiques(nombres)
  nombres_pairs_result = nombres_pairs(nombres)
  print(f"Somme des nombres : {somme}")
  print(f"Moyenne des nombres : {moyenne}")
  print(f"Nombre de nombres supérieurs à la moyenne : {nombres_supérieurs}")
  print(f"Nombre de nombres pairs : {nombres_pairs_result}")


main()