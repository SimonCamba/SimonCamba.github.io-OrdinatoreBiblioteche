import csv

def leggiCSV(file):
    with open(file,"r") as miocsv:
        a=list(csv.reader(miocsv, delimiter=","))
        return a
tabella=leggiCSV('anagrafica_biblioteche.csv')

def lista_tipologie(var):
    tipAmm=[]
    for row in var[1:]:
        tipAmm.append(row[3])
    b=list(set(tipAmm))
    return b

categorie=lista_tipologie(tabella)

def filtroTipAmm(var,str):
    nomefile="biblioteche_categoria_"+str+'.csv'
    with open(nomefile, "w", newline='') as mycsv:
        for row in var:
            if str in row:
                scrittore = csv.writer(mycsv, delimiter=";")
                scrittore.writerow(row)
    righe=0
    for row in nomefile:
        righe+=1
    print(f"Le biblioteche appartenenti alla tipologia amministrativa {str} sono: {righe}")

for el in categorie:
    filtroTipAmm(tabella, el)
