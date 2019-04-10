#Script de conversion d'une entrée ASM à un code exécutable par le processeur ternaire

#CdC - Lecture de fichiers texte .truitep
# format ASM : 0: OPT OPERAND OPERAND
#              1: OPT OPERAND OPERAND
#              3: OPT OPERAND OPERAND
#              ....
# Fichier d'architecture (JSON)
#Sort un dictionnaire JSON de mots TCD (ternaire codé décimal) mémoire pour clé adresse mémoire séquentielle affecte un mot

import json
from tkinter import *
from tkinter.filedialog import askopenfilename

#Load architecture specifications
def loadArchi():
    global archi
    filename = askopenfilename(title="Ouvrir un fichier architecture",filetypes=[('truitea files','*.truitea'),('all files','*.*')])
    farchi = open(filename,"r")
    archi =  json.load (farchi)
    farchi.close()
    return 0

#Load assembly file
def loadASM():
    global assembly
    filenameASM = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
    fspec = open(filenameASM,"r")
    assembly = fspec.readlines()
    fspec.close()
    return 0

#Export implementation file
def exportBin():
    return 0

def convert() :
    return 0

fenetre = Tk()

#Architecture frames
Frame1  = Frame(fenetre)
Frame1.pack(side = LEFT, padx=30, pady= 30)

Frame2  = Frame(fenetre)
Frame2.pack(side = LEFT, padx=30, pady=30)

Frame3 = Frame(fenetre)
Frame3.pack(side = RIGHT, padx=30, pady= 30)

Frame4 = Frame(fenetre)
Frame4.pack(side= BOTTOM, padx = 30, pady=30)

#Frame1
labelArchi = Label(Frame1, text = "Fichier architecture").pack()
boutonArchi=Button(Frame1, text="Charger", command=loadArchi).pack()
#Frame2
labelASM = Label(Frame2, text = "Fichier assembleur").pack()
boutonASM = Button(Frame2, text = "Charger", command=loadASM).pack()
#Frame3
labelExp = Label(Frame3, text = "Exporter sous...")
boutonExp = Button(Frame3, text = "Emplacement", command = exportBin).pack()
#Frame4
boutonOp = Button(Frame4, text  ="Convertir", command = convert).pack()

fenetre.mainloop()

