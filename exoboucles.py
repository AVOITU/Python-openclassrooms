print("Saisisez une série de chiffres entier séparés par des  virgules et mettre aucun espace, par exemple 1,2,3,4")
saisie=input()

separation=saisie.split(',')

calcul=0

for somme in separation :
  calcul=int(somme)+calcul

print(f"somme des nombres: {calcul}")

moyenne=calcul/len(separation)
print(f"Moyenne des nombres: {moyenne}")


nombres_supérieurs=0
for superieur in separation :
  if int(superieur)>moyenne :
    nombres_supérieurs=nombres_supérieurs+1


print(f"Nombre de nombres supérieurs à la moyenne: {nombres_supérieurs}")


nombres_pairs=0
indice=0
while indice<len(separation) :
  if int(separation[indice])%2==0 :
    nombres_pairs=nombres_pairs+1
    indice=indice+1
  else :
    indice=indice+1

print(f"Nombre de nombres pairs: {nombres_pairs}")