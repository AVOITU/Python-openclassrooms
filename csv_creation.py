import csv

def extract():
  #Extract initial informations from the file and put it under a form of list of dictionnaries
  with open("input.csv", mode="r", newline="", encoding= "utf-8") as file:
    csv_reader = list(csv.DictReader(file))
  
  return csv_reader

def transform(csv_reader):
  #transform the data in the list of dictionnaries, l.14 is here to conserve csv_reader in case of a need of information in a later work
  modified_data = csv_reader
  for row in modified_data:
    data=int(row['heures_travaillees']) * 15
    row["heures_travaillees"]=data

  return modified_data

def load(modified_data):
  #write the new csv file with the new informations
  en_tete=["nom","heures_travaillees"]
  with open ("output.csv", mode="w") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(en_tete)
    for row in modified_data:
      row_data = [row[key] for key in en_tete]
      writer.writerow(row_data)

def main():
  csv_reader = extract()
  modified_data = transform(csv_reader)
  load(modified_data)

if __name__ == "__main__":
  main()