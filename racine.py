from PyQt5.uic import loadUi
from math import *
from pickle import load,dump
from PyQt5.QtWidgets import *
def cherchep(x):
    p=1
    while(p**2 <=x):
        p=p+1
    return p-1






















def add_click():
    x=w.inp.text()
    if(len(x)==0):
        QMessageBox.critical( w , "erreur" ,"veuillez saisir une valeur pour X " )
    elif (float(x)<2 or float(x)>200):
        QMessageBox.critical( w , "erreur" ,"veuillez saisir une valeur entre 2 et 200" )
    else:
        s=cherchep(float(x))
        s1=1/2*(s+float(x)/s)
        while (abs(s1-s)>0.00001):
            s=s1
            s1=1/2*(s+float(x)/s)
        f=open("approche.dat","ab")
        t={}
        t["X"]=x
        t["RC"]=s1
        dump(t,f)
        QMessageBox.information( w , "Succés" ,"Enregisté avec succés" )
        w.inp.clear()
        f.close()
def afficher_click():
    y=open("approche.dat","rb")
    ligne=0
    Fin_fichier = False
    while  Fin_fichier ==False :
        try :
            x=load(y)
            print(x)
            w.lst.setRowCount(ligne+1)
            w.lst.setItem(ligne,0,QTableWidgetItem(str(float(x["X"]))))
            w.lst.setItem(ligne,1,QTableWidgetItem(str(x["RC"])))
            ligne+=1
        except :
            Fin_fichier = True
    y.close()
app = QApplication([])
w = loadUi ("./inter.ui")
w.show()
w.add.clicked.connect ( add_click )
w.afficher.clicked.connect ( afficher_click )
app.exec_()