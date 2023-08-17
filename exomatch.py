print("Choissez un nombre entier")
nombre_a_gauche=input()


if nombre_a_gauche.isnumeric()==False :
  print("Erreur: les deux nombres doivent être des nombres entiers")


nombre_a_gauche=int(nombre_a_gauche)

print("Choissisez un autre nombre entier")
nombre_a_droite=input()

if nombre_a_droite.isnumeric()==False :
  print("Erreur: les deux nombres doivent être des nombres entiers")
  

nombre_a_droite=int(nombre_a_droite)  

print("Choissisez entre +, -, * ou /")
operation=input()

match operation:
  case "+" :
    résultat=(nombre_a_gauche+nombre_a_droite)
    print(résultat)
  case "-" :
    résultat=(nombre_a_gauche-nombre_a_droite)
    print(résultat)
  case "*" :
    résultat=(nombre_a_gauche*nombre_a_droite)
    print(résultat)
  case "/" :
    if nombre_a_droite==0 :
      print("Erreur: impossible de diviser par zéro.")
      exit()
    else :
      résultat=(nombre_a_gauche/nombre_a_droite)
      print(résultat)
  case _ :
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'")
    exit()