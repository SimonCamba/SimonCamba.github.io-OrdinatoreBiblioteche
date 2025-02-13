import csv

def leggiCSV(file):
    with open(file,"r") as miocsv:
        a=list(csv.reader(miocsv, delimiter=","))
        return a
tabella=leggiCSV('anagrafica_biblioteche.csv')

def lista_tipologie(var):
    t=[row[3] for row in var[1:]]
    tipologie=list(set(t))
    return tipologie

tipAmm=lista_tipologie(tabella)

def FileTipAmm(var,type):
    nomefile = f"biblioteche_categoria_{type}.csv"
    with open(nomefile, "w", newline="") as miocsv:
        for row in var:
            if type in row:
                scrittore = csv.writer(miocsv, delimiter=",")
                scrittore.writerow(row)
    print(f"Le biblioteche appartenenti alla tipologia amministrativa {type} sono: {len(nomefile)}")
FileTipAmm(tabella,"Enti locali")

for el in tipAmm:
    FileTipAmm(tabella,el)
