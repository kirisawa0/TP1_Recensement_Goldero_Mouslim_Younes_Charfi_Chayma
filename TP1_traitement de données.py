from pylab import figure
from pylab import plot
from pylab import show



fic= open("donnees_2016.csv","r",encoding="UTF-8")
L2016=[]
aglotot={"Appoigny", "Augy", "Auxerre", "Bleigny-le-Carreau", "Branches", "Champs-sur-Yonne", "Charbuy","Chevannes", "Chitry", "Coulanges-la-Vineuse", "Escamps", "Escolives Sainte-Camille","Gurgy","Gy-l’Evêque", "Irancy", "Jussy", "Lindry", "Monéteau", "Montigny-la-Resle", "Perrigny", "Quenne,Saint-Bris-le-Vineux", "Saint-Georges-sur-Baulche", "Vallan", "Venoy", "Villefargeau", "Villeneuve-Saint-Salves", "Vincelles", "Vincelottes"}
# ici on a crée un dico pour pouvoir selectionner que les communes qui nous interessent
for i in range(35383):                                           #Lancement des listes 
    a=fic.readline().strip().split(',')
    if i>0:
        if a[6] in aglotot:
            L2016.append([a[6],a[0],a[1],str(int(a[2])*1000+int(a[5])),a[5],a[9]])


              
fic.close


fic= open("donnees_2008.csv","r",encoding="UTF-8")
L2008=[]

for i in range(36725):
    a=fic.readline().strip().split(',')
    if i >0:
        if a[6] in aglotot:
            L2008.append([a[6],a[0],a[1],str(int(a[2])*1000+int(a[5])),a[5],a[9]])

              
fic.close


Lcomtot=[]                                              # Lancement d'une liste contenant le numéro des communes dont on a besoin 
for i in range(len(L2008)):
    Lcomtot.append(L2008[i][3])


fic= open("donnees_2021.csv","r",encoding="UTF-8")

L2021=[]

for i in range(34991):
    a=fic.readline().strip().split(';')
    if i>0:
        if a[2] in Lcomtot:   
            L2021.append([a[0],a[1],a[2],a[3],a[4],a[5]])
    

              
fic.close

#Agglomeration totale d'auxerre évolution

Levo=[]                                                #Levo est une liste qui contient la population aux différentes années pour les mettre ensuite dans le graphique

print("population de l'aglomération totale :")


poptot2008=0
for i in range(len(L2008)):              # Ici le calcul de la population totale pour 2008  
    if L2008[i][0] in aglotot:
        poptot2008+=int(L2008[i][5])
Levo.append(poptot2008)
print(poptot2008)


poptot2016=0
for i in range(len(L2016)):
    if L2016[i][0] in aglotot:
        poptot2016+=int(L2016[i][5])
Levo.append(poptot2016)
print(poptot2016)

poptot2021=0
for i in range(len(L2021)):
    if L2021[i][2] in Lcomtot  :
       poptot2021+=int(L2021[i][5])
Levo.append(poptot2021)
print(poptot2021)

figure()
plot([2008,2016,2021],Levo)         # Lancement du graphique
show()


#Agglomeration immédiate d'auxerre évolution

agloim={"Appoigny","Auxerre", "Monéteau", "Perrigny", "Saint-Georges-sur-Baulche"}  # Ce dico nous sert a limiter la selection aux communes de l'agglomeration immédiate d'auxerre

Lcomim=[]                                     # Cette liste a le même fonctionnement que notre dico précédent mais lui il sert uniquement pour 2021
for i in range(len(L2008)):
    if L2008[i][0] in agloim:
        Lcomim.append(L2008[i][3])


Levo=[]                                        #On réinitialise Levo pour éviter la confusion
print("population de l'aglomération immédiate :")


poptot2008=0
for i in range(len(L2008)):
    if L2008[i][0] in agloim:
        poptot2008+=int(L2008[i][5])
Levo.append(poptot2008)
print(poptot2008)


poptot2016=0
for i in range(len(L2016)):
    if L2016[i][0] in agloim:
        poptot2016+=int(L2016[i][5])
Levo.append(poptot2016)
print(poptot2016)

poptot2021=0
for i in range(len(L2021)):
    if L2021[i][2] in Lcomim  :
       poptot2021+=int(L2021[i][5])
Levo.append(poptot2021)
print(poptot2021)

figure()
plot([2008,2016,2021],Levo)          # Lancement du graphique
show()


#Auxerre évlution
Levo=[]
print("population d'auxerre :")

poptot2008=0
for i in range(len(L2008)):
    if L2008[i][0] in 'Auxerre':
        poptot2008+=int(L2008[i][5])
Levo.append(poptot2008)       
print(poptot2008)


poptot2016=0
for i in range(len(L2016)):
    if L2016[i][0]=='Auxerre':
        poptot2016+=int(L2016[i][5])
Levo.append(poptot2016)
print(poptot2016)

poptot2021=0
for i in range(len(L2021)):
    if L2021[i][2] == '89024'  :
       poptot2021+=int(L2021[i][5])
Levo.append(poptot2021)
print(poptot2021)

figure()
plot([2008,2016,2021],Levo)                  # Lancement du graphique
show()
