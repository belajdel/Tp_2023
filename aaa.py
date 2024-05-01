from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from pickle import *

def cherchp (x):
    p=1
    while p**2<=x:
        p=p+1
    return p-1

def appro (x):
    s1=cherchp(float(x))
    s2=1/2*(s1+x/s1)
    while abs(s2-s1)>=0.00001:
        s1=s2
        s2=1/2*(s1+x/s1)
    return s2
        
def add_click():
    x=windows.inp.text()
    if len(x)==0:
        QMessageBox.critical(windows,"erruer","ekteb asba")
    elif float(x)<2 or float(x)>200:
        QMessageBox.critical(windows,"erruer","ekteb mabin 2 o 200")
    else:
        d={}
        d["x"]=float(x)
        d["rc"]=appro(float(x))
        f=open("rc.dat","ab")
        dump(d,f)
        QMessageBox.information(windows,"mabrouk","hak hchitou")
    f.close()
        
        

        
def afficher_click():
    f=open("rc.dat","rb")
    fin= False
    l=0
    while fin == False:
        try:
            x=load(f)
            print(x)
            windows.lst.setRowCount(l+1)
            windows.lst.setItem(l,0,QTableWidgetItem(str(float(x["x"]))))
            windows.lst.setItem(l,1,QTableWidgetItem(str(x["rc"])))
            l=l+1
        except:
            fin= True
    f.close()
        
    









app = QApplication([])
windows = loadUi ("C:/Users/Administrator/Desktop/pratiqu rev/bac2023[working]/inter.ui")
windows.show()
windows.add.clicked.connect ( add_click )
windows.afficher.clicked.connect ( afficher_click )

app.exec_()