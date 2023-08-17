print("Choissez un nombre entier")
nombre_a_gauche=input()

if nombre_a_gauche.isnumeric()==False :
  print("Erreur: les deux nombres doivent être des nombres entiers")


print("Choissisez un nombre entier")
nombre_a_droite=input()

if nombre_a_droite.isnumeric()==False :
  print("Erreur: les deux nombres doivent être des nombres entiers")
  

print("Choissisez entre +, -, * ou /")
operation=input()

match operation:
  case "+" :
    résultat=(nombre_a_gauche+nombre_a_droite)
  case "-" :
    résultat=(nombre_a_gauche-nombre_a_droite)
  case "*" :
    résultat=(nombre_a_gauche*nombre_a_droite)
  case "/" :
    résultat=(nombre_a_gauche/nombre_a_droite)
