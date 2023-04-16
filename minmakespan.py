# Algorithme du Min-Makespan et du Semi-fast Makespan
# Placé Louka
# Versio du 21 / 11 / 2022

#----Import----
import random
import math
import copy
from math import *


#===============================Fonction Saisir_entre================================================
def saisir_entre(dmin,dmax):
    for i in range(n):
        D[i] = (int(random.randrange(dmin,dmax)))

#===============================Fonction Saisir_entre_semifast=======================================
def saisir_entre_semifast(dmin,dmax):
    dmin =dmin/2
    dmax = dmax/2
    for i in range(n):
        D[i] = (random.randint(dmin,dmax)) * 2

#===================================Fonction LSA=====================================================
def LSA(D,M,m):
    y = 0 #index pour le tableau des tâches
    i = 0 #index pour le tableau des machines (en fonction de celui des tâches)
    x = 0 #valeur minimum du tableau des machines
    c = 0 # somme durée des tâches
    borneinfmax = max(D) # Borne inférieur "maximum"
    borneinfmoy = 0 # Borne inférieur "minimum"
    global Tlsa #Variable global qu'on va récupérer pour faire la moyenne des ratios dans l'algo principal

    # Boucle while qui attribue les tâches aux machines !
    while y < n :
        if i >= len(M):     #Si l'index i est supérieur à la longueur du tableau de machine
            x = min(M)      #Alors il va chercher la plus petite valeur dans ce tableau
            #print("\n")
            #print('La tâche qui dure' ,x,' sera finit en première')
            z = M.index(x)
            #print('La tâche suivante sera effectué par la machine :',z+1)
            M[z] = M[z] + D[y]
            c = c + D[y]
            #print(c)
            D[y]=0
            y = y + 1
            i = i + 1

            #print(D)
            #print(M)
        else:
            M[y] = M[y] + D[y]
            c = c + D[y]
            #print(c)
            D[y]=0
            y = y + 1
            i = i + 1
            #print("\n")
            #print(D)
            #print(M)

    borneinfmoy = c/m # Résultat de la borne inférieur moyenne
    borneinfmoy = ceil(borneinfmoy)
    B = 0 #Diviseur de Tlsa
    #print ('La borne inférieur maximum est ', borneinfmax,'et la borne inférieur moyenne est ',borneinfmoy,'.')
    if borneinfmax > borneinfmoy :
        B = borneinfmax
        #print('On va prendre la borne maximum',borneinfmax,', car sa valeur est supérieur pour calculer le ratio Moyen')
    else :
        B = borneinfmoy
        #print('On va prendre la borne moyenne',borneinfmoy,', car sa valeur est supérieur pour calculer le ratio Moyen')

    #print('Le temps maximum pour effectuer toutes les tâches est de', max(M),' pour l`algorithme du LSA. \n')
    #print('le max de M est',max(M))
    #print(B)
    Tlsa = (max(M))/B
    #print('Le ratio LSA est ',Tlsa,'.')

#===================================Fonction LSA-semifast============================================

def LSAsemi(D,M,m):
    y = 0 #index pour le tableau des tâches
    i = 0 #index pour le tableau des machines (en fonction de celui des tâches)
    x = 0 #valeur minimum du tableau des machines
    c = 0 # somme durée des tâches
    borneinfmax = (max(D))/2 # Borne inférieur "maximum"
    borneinfmoy = 0 # Borne inférieur "minimum" (résultat plus bas)
    global Tlsasemi

    # Boucle while qui attribue les tâches aux machines !
    while y < n :
        if i >= len(M):
            x = min(M)
            #print('La tâche qui dure' ,x,' sera finit en première')
            z = M.index(x)
            #print('La tâche suivante sera effectué par la machine :',z+1)
            if M.index(min(M)) < m/2 :
                #print('Elle ira 2 fois plus vite pour effectuer la tâche !!')
                M[z] = M[z] + (D[y]/2)
                c = c + (D[y])/2
                #print(c)
                D[y]=0
                y = y + 1
                i = i + 1
                #print("\n")
                #print(D)
                #print(M)
            else :
                M[z] = M[z] + D[y]
                c = c + D[y]
                #print(c)
                D[y]=0
                y = y + 1
                i = i + 1
                #print("\n")
                #print(D)
                #print(M)
        else:
            if 0 <= i and i < m/2 :
                #print('Elle ira 2 fois plus vite pour effectuer la tâche !!')
                #print('La tâche suivante sera effectué par la machine :',z)
                M[y] = M[y] + (D[y]/2)
                c = c + (D[y])/2
                #print(c)
                D[y]=0
                y = y + 1
                i = i + 1
                #print("\n")
                #print(D)
                #print(M)
            else :
                M[y] = M[y] + D[y]
                c = c + D[y]
                #print(c)
                D[y]=0
                y = y + 1
                i = i + 1
                #print("\n")
                #print(D)
                #print(M)
    borneinfmoy = (2/3)*(c/m) # Résultat de la borne inférieur moyenne
    borneinfmoy = ceil(borneinfmoy)
    B = 0 #Diviseur de Tlsasemi
    #print ('La borne inférieur maximum est ', borneinfmax,'et la borne inférieur moyenne est ',borneinfmoy,'.')
    if borneinfmax > borneinfmoy :
        B = borneinfmax
        #print('On va prendre la borne maximum',borneinfmax,', car sa valeur est supérieur pour calculer le ratio Moyen')
    else :
        B = borneinfmoy
        #print('On va prendre la borne moyenne',borneinfmoy,', car sa valeur est supérieur pour calculer le ratio Moyen')

    #print('Le temps maximum pour effectuer toutes les tâches est de', max(M),' pour l`algorithme du LSA. \n')
    Tlsasemi = (max(M))/B
    #print('Le ratio LSA (semi-fast) est ',Tlsasemi,'.')

#===================================Fonction LPT============================================

def LPT(D,M,m):
    y = 0 #index pour le tableau des tâches
    i = 0 #index pour le tableau des machines (en fonction de celui des tâches)
    x = 0 #valeur minimum du tableau des machines
    c = 0 # somme durée des tâches
    borneinfmax = max(D) # Borne inférieur "maximum"
    borneinfmoy = 0 # Borne inférieur "minimum" (résultat plus bas)
    global Tlpt

    # Boucle while qui attribue les tâches aux machines !
    while y < n :
        if i >= len(M):
            x = min(M)
            #print("\n")
            #print('La tâche qui dure' ,x,' sera finit en première')
            z = M.index(x)
            #print('La tâche suivante sera effectué par la machine :',z+1)
            M[z] = M[z] + D[y]
            c = c + D[y]
            #print(c)
            D[y]=0
            y = y + 1
            i = i + 1
            #print(D)
            #print(M)
        else:
            M[y] = M[y] + D[y]
            c = c + D[y]
            #print(c)
            D[y]=0
            y = y + 1
            i = i + 1
            #print("\n")
            #print(D)
            #print(M)
    borneinfmoy = c/m # Résultat de la borne inférieur moyenne
    borneinfmoy = ceil(borneinfmoy)
    B = 0 #Diviseur de Tlpt

    #print ('La borne inférieur maximum est ', borneinfmax,'et la borne inférieur moyenne est ',borneinfmoy,'.')
    if borneinfmax > borneinfmoy :
        B = borneinfmax
        #print('On va prendre la borne maximum',borneinfmax,', car sa valeur est supérieur pour calculer le ratio Moyen')
    else :
        B = borneinfmoy
        #print('On va prendre la borne moyenne',borneinfmoy,', car sa valeur est supérieur pour calculer le ratio Moyen')

    #print('Le temps maximum pour effectuer toutes les tâches est de', max(M),' pour l`algorithme du LPT. \n')
    Tlpt = (max(M))/B
    #print('Le ratio LPT est ',Tlpt,'.')

#===================================Fonction LPT semifast============================================

def LPTsemi(D,M,m):
    y = 0 #index pour le tableau des tâches
    i = 0 #index pour le tableau des machines (en fonction de celui des tâches)
    x = 0 #valeur minimum du tableau des machines
    c = 0 # somme durée des tâches ADD
    borneinfmax = (max(D))/2 # Borne inférieur "maximum"
    borneinfmoy = 0 # Borne inférieur "moyenne" (résultat plus bas)
    global Tlptsemi

    # Boucle while qui attribue les tâches aux machines !
    while y < n :
        if i >= len(M):
            x = min(M)
            #print('La tâche qui dure' ,x,' sera finit en première')
            z = M.index(x)
            #print('La tâche suivante sera effectué par la machine :',z+1)
            if M.index(min(M)) < m/2 :
                #print('Elle ira 2 fois plus vite pour effectuer la tâche !!')
                M[z] = M[z] + (D[y]/2)
                c = c + (D[y])/2
                #print(c)
                D[y]=0
                y = y + 1
                i = i + 1
                #print("\n")
                #print(D)
                #print(M)
            else :
                M[z] = M[z] + D[y]
                c = c + D[y]
                #print(c)
                D[y]=0
                y = y + 1
                i = i + 1
                #print("\n")
                #print(D)
                #print(M)

        else:
            if M.index(min(M)) < m/2 :
                #print('Elle ira 2 fois plus vite pour effectuer la tâche !!')
                M[y] = M[y] + (D[y])/2
                c = c + (D[y])/2
                #print(c)
                D[y]=0
                y = y + 1
                i = i + 1
                #print("\n")
                #print(D)
                #print(M)
            else :
                M[y] = M[y] +D[y]
                c = c + D[y]
                #print(c)
                D[y]=0
                y = y + 1
                i = i + 1
                #print("\n")
                #print(D)
                #print(M)
    borneinfmoy = (2/3)*(c/m) # Résultat de la borne inférieur moyenne
    borneinfmoy = ceil(borneinfmoy)
    B = 0 #Diviseur de Tlptsemi

    #print ('La borne inférieur maximum est ', borneinfmax,'et la borne inférieur moyenne est ',borneinfmoy,'.')
    if borneinfmax > borneinfmoy :
        B = borneinfmax
        #print('On va prendre la borne maximum',borneinfmax,', car sa valeur est supérieur pour calculer le ratio Moyen')
    else :
        B = borneinfmoy
        #print('On va prendre la borne moyenne',borneinfmoy,', car sa valeur est supérieur pour calculer le ratio Moyen')

    #print('Le temps maximum pour effectuer toutes les tâches est de', max(M),' pour l`algorithme du LSA. \n')
    Tlptsemi = (max(M))/B
    #print('Le ratio LPT (semi-fast) est ',Tlptsemi,'.')

#===================================Fonction RMA============================================

def RMA(D,M,m):
    y = 0 #index pour le tableau des tâches
    c = 0 # somme durée des tâches
    borneinfmax = max(D) # Borne inférieur "maximum"
    borneinfmoy = 0 # Borne inférieur "moyenne" (résultat plus bas)
    global Trma

    # Boucle while qui attribue les tâches aux machines !
    while y < n :
        z=random.randint(0,m-1)
        x = D[y]
        #print('la machine ',z+1,'va effectuer la tâche qui dure ',x)
        M[z] = M[z] + D[y]
        c = c + D[y]
        #print(c)
        D[y]=0
        y = y + 1
        #print("\n")
        #print(D)
        #print(M)

    borneinfmoy = c/m # Résultat de la borne inférieur moyenne
    B = 0 #Diviseur de Trma
    borneinfmoy = ceil(borneinfmoy)

    #print ('La borne inférieur maximum est ', borneinfmax,'et la borne inférieur moyenne est ',borneinfmoy,'.')
    if borneinfmax > borneinfmoy :
        B = borneinfmax
        #print('On va prendre la borne maximum',borneinfmax,', car sa valeur est supérieur pour calculer le ratio Moyen')
    else :
        B = borneinfmoy
        #print('On va prendre la borne moyenne',borneinfmoy,', car sa valeur est supérieur pour calculer le ratio Moyen')

    #print('Le temps maximum pour effectuer toutes les tâches est de', max(M),' pour l`algorithme du LSA. \n')
    Trma = (max(M))/B
    #print('Le ratio RMA est ',Trma,'(arrondis à l`entier supérieur).')

#===================================Fonction RMA semifast============================================

def RMAsemi(D,M,m):
    y = 0 #index pour le tableau des tâches
    c = 0 # somme durée des tâches
    borneinfmax = (max(D))/2 # Borne inférieur "maximum"
    borneinfmoy = 0 # Borne inférieur "moyenne" (résultat plus bas)
    global Trmasemi

    # Boucle while qui attribue les tâches aux machines !
    while y < n :
        z=random.randint(0,m-1)
        #print("\n")
        x = D[y]
        #print('la machine ',z+1,'va effectuer la tâche qui dure ',x)
        if z < m/2 :
            #print('Elle ira 2 fois plus vite pour effectuer la tâche !!')
            M[z] = M[z] + (D[y])/2
            c = c + (D[y])/2
            #print(c)
            D[y]=0
            y = y + 1
            #print(D)
            #print(M)
        else:
            M[z] = M[z] + D[y]
            c = c + D[y]
            #print(c)
            D[y]=0
            y = y + 1
            #print(D)
            #print(M)
    borneinfmoy = (2/3)*(c/m) # Résultat de la borne inférieur moyenne
    B = 0 #Diviseur de Trmasemi
    borneinfmoy = ceil(borneinfmoy)
    #print ('La borne inférieur maximum est ', borneinfmax,'et la borne inférieur moyenne est ',borneinfmoy,'.')
    if borneinfmax > borneinfmoy :
        B = borneinfmax
        #print('On va prendre la borne maximum',borneinfmax,', car sa valeur est supérieur pour calculer le ratio Moyen')
    else :
        B = borneinfmoy
        #print('On va prendre la borne moyenne',borneinfmoy,', car sa valeur est supérieur pour calculer le ratio Moyen')

    #print('Le temps maximum pour effectuer toutes les tâches est de', max(M),' pour l`algorithme du LSA. \n')
    Trmasemi = (max(M))/B
    #print('Le ratio RMA (semi-fast) est ',Trmasemi,'.')

#|==============================================================================================|
#|=====================================Programme Principal======================================|
#|==============================================================================================|

#Initialise les variables
MoyenneRatioLSA = 0
MoyenneRatioLPT = 0
MoyenneRatioRMA = 0

MoyenneRatioLSAsemi = 0
MoyenneRatioLPTsemi = 0
MoyenneRatioRMAsemi = 0

choix = 0

# Condition vérifié si l'user tape 1 ou 2
while choix != 1 and choix !=2 :
    choix = int(input('Tapez 1 pour le problème du Min-Maskespan et 2 pour le Semi-Fast'))

if choix ==1 : #Si tape 1 (alors min-makespan)

    dmin = 0 #variable dmin
    dmax = 1 #variable dmax
    m = 0    # variable du nombre de machine
    n = 0    # variable du nombre de tâche
    k = 0    # variable du nombre d'instance

    while m <= 0:
        m = int(input('Entrez le nombre de machine(s) ')) # Nombre de machine
    while n <= 0:
        n = int(input('Entrez le nombre de tâche(s) '))   # Nombre de tâches
    while k <= 0:
        k = int(input('Entrez le nombre d`instances(s) '))# Nombre d'instances
    D = n*[0] # On déclare le tableau des tâche et leur durées
    M = m*[0] # On déclare le tableau qui représente chacune des machine
    M1 = copy.copy(M)
    M2 = copy.copy(M)

    #Boucle while pour vérifier que la durée min soit supérieur à 1
    while dmin < 1 :
        dmin = int(input('Entrez la durée minimum d`une tâche '))

    #Boucle while pour vérifier que la durée max soit supérieur à la durée min
    while dmax <= dmin :
        dmax = int(input('Entrez la durée maximum d`une tâche '))


    #------------Affichage des valeurs------------
    print ('____________/ Vos données \_____________')
    print ('Votre nombre de machine(s) est',m)
    print ('Votre nombre de tâche(s) est',n)
    print ('Votre nombre d`instances(s) est',k)
    print ('La durée d`une tâche est comprise entre',dmin,'et',dmax)

    #boucle pour chaque k instance
    for i in range(k):
        #print ('~~~~~~~~~~~~~~~~Instance n°',i+1,'~~~~~~~~~~~~~~~~\n')
        saisir_entre(dmin,dmax) # Appel de la fonction saisir_entre qui entre aléatoirement
                                # des valeurs dans l'interval dmin et dmax dans le tableau de Tâche

        #------------------------------------------
        #Les algorithmes :
        #print('========================ALGORITHME LSA',i+1,'========================')
        #print ('Durée des tâches à effectuer (LSA) : ',D)
        #print ('La/Les mâchine(s) :', M)
        D1 = copy.copy(D) # Copie du tableau D pour algo LPT
        D2 = copy.copy(D) # Copie du tableau D pour algo RMA
        LSA(D,M,m) #LSA
        MoyenneRatioLSA = MoyenneRatioLSA + Tlsa
        #print('Somme des ratios des LSA :',MoyenneRatioLSA)

        #print ('========================ALGORITHME LPT',i+1,'========================')
        D1.sort(reverse = True)
        #print ('Durée des tâches triés dans l`ordre décroissant(LPT) :' ,D1)
        #print ('La/Les mâchine(s) :', M1)
        LPT(D1,M1,m) #LPT
        MoyenneRatioLPT = MoyenneRatioLPT + Tlpt
        #print('Somme des ratios des LPT:',MoyenneRatioLPT)

        #print('========================ALGORITHME RMA',i+1,'========================')
        #print ('Durée des tâches à attribuer dans un ordre au hasard au(x) machine(s):' , D2)
        #print ('La/Les mâchine(s) :', M2)
        RMA(D2,M2,m) #RMA
        MoyenneRatioRMA = MoyenneRatioRMA + Trma
        #print('Somme des ratios des RMA :',MoyenneRatioRMA)
        # Reset des tableaux des machines !
        for i in range(m):
            M[i] = 0
            M1[i] = 0
            M2[i] = 0

    #Affichange des Moyenne des ratios LSA/LPT/RMA en semifastmakespan
    print('==============Les Moyennes des ratios ================')
    print('Somme des ratios des LSA :',MoyenneRatioLSA)
    MoyenneRatioLSA = MoyenneRatioLSA/k
    print("La moyenne des ratios LSA :",MoyenneRatioLSA)

    print('Somme des ratios des LPT :',MoyenneRatioLPT)
    MoyenneRatioLPT = MoyenneRatioLPT/k
    print("La moyenne des ratios LPT :",MoyenneRatioLPT)

    print('Somme des ratios des RMA :',MoyenneRatioRMA)
    MoyenneRatioRMA = MoyenneRatioRMA/k
    print("La moyenne des ratios RMA :",MoyenneRatioRMA)

else : #Sinon tape 2 (alors semifast-makespan)

    n = 0    # variable du nombre de tâche
    k = 0    # variable du nombre d'instance
    dmin = 0 #variable dmin
    dmax = 1 #variable dmax
    m=1      # variable d nombre de machine
    # Condition pour que le nombre de machine soit paire
    while m%2 != 0 or m <=0 :
        m = int(input('Entrez le nombre de machine(s) '))
    while n <= 0:
        n = int(input('Entrez le nombre de tâche(s) '))   # Nombre de tâches
    while k <= 0:
        k = int(input('Entrez le nombre d`instances(s) '))# Nombre d'instances
    D = n*[0] # On déclare le tableau des tâche et leur durées
    M = m*[0] # On déclare le tableau qui représente chacune des machine
    M1 = copy.copy(M)
    M2 = copy.copy(M)

    #Boucle while pour vérifier que la durée min soit supérieur à 1 et PAIRE
    while dmin < 1 or dmin%2 != 0 :
        dmin = int(input('Entrez la durée minimum d`une tâche '))

    #Boucle while pour vérifier que la durée max soit supérieur à la durée min ET paire
    while dmax <= dmin or dmax%2 != 0 :
        dmax = int(input('Entrez la durée maximum d`une tâche '))




    #------------Affichage des valeurs------------
    print ('____________/ Vos données \_____________')
    print ('Votre nombre de machine(s) est',m)
    print ('Votre nombre de tâche(s) est',n)
    print ('Votre nombre d`instances(s) est',k)
    print ('La durée d`une tâche est comprise entre',dmin,'et',dmax)

    #boucle for pour k instance
    for i in range(k):
        #print ('~~~~~~~~~~~~~~~~Instance n°',i+1,'~~~~~~~~~~~~~~~~\n')
        saisir_entre_semifast(dmin,dmax)# Appel de la fonction saisir_entre_semifast qui entre aléatoirement
                                        # des valeurs paire dans l'interval dmin et dmax dans le tableau des Tâches


        #Les algorithmes :
        #print('========================ALGORITHME LSA (semi fast)',i+1,'========================')
        #print ('Durée des tâches à effectuer (LSA) : ',D)
        #print ('La/Les mâchine(s) :', M)
        D1 = copy.copy(D) # Copie du tableau D pour algo LPT
        D2 = copy.copy(D) # Copie du tableau D pour algo RMA
        LSAsemi(D,M,m) #LSA semi fast
        MoyenneRatioLSAsemi = MoyenneRatioLSAsemi + Tlsasemi
        #print('Somme des ratios LSA-semi :',MoyenneRatioLSAsemi)

        #print ('========================ALGORITHME LPT (semi fast)',i+1,'========================')
        D1.sort(reverse = True)
        #print ('Durée des tâches triés dans l`ordre décroissant(LPT) :' ,D1)
        #print ('La/Les mâchine(s) :', M1)
        LPTsemi(D1,M1,m) #LPT semi fast
        MoyenneRatioLPTsemi = MoyenneRatioLPTsemi + Tlptsemi
        ##print('Somme des ratios LPT-semi :',MoyenneRatioLPTsemi)

        #print('========================ALGORITHME RMA (semi fast)',i+1,'========================')
        #print ('Durée des tâches à attribuer dans un ordre au hasard au(x) machine(s):' , D2)
        #print ('La/Les mâchine(s) :', M2)
        RMAsemi(D2,M2,m) #RMA semi fast
        MoyenneRatioRMAsemi = MoyenneRatioRMAsemi + Trmasemi
        #print('Somme des ratios RMA-semi :',MoyenneRatioRMAsemi)
        #boucle pour reset tableaux des machines
        for i in range(m):
            M[i] = 0
            M1[i] = 0
            M2[i] = 0
    #Affichange des Moyenne des ratios LSA/LPT/RMA en semifastmakespan
    print('==============Les Moyennes des ratios :================')

    MoyenneRatioLSAsemi = MoyenneRatioLSAsemi/k
    print("La moyenne des ratios LSA-semi :",MoyenneRatioLSAsemi)

    MoyenneRatioLPTsemi = MoyenneRatioLPTsemi/k
    print("La moyenne des ratios LPT-semi :",MoyenneRatioLPTsemi)

    MoyenneRatioRMAsemi = MoyenneRatioRMAsemi/k
    print("La moyenne des ratios RMA-semi :",MoyenneRatioRMAsemi)




