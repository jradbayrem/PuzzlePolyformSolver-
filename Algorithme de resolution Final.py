# -*- coding: cp1256 -*-
import itertools
import numpy as np
from copy import deepcopy
class AlgorithmeReso:

    
 totalListPieceNonAscied=[]
 totalListPiece=[]
 totalPiecesDeplacements=[]
 totalCombinaison=[]

 
 def trasfTTMatAsci(self,totalListPieceNonAscied):
     ttPiece=[]
     for x in range(len(totalListPieceNonAscied)):
         ttPiece.append(self.transfMatriceAscii(deepcopy(totalListPieceNonAscied[x])))
     return ttPiece




 def transfAsciedMat(self,liste):
     for i in range(len(liste)):
         for j in range(len(liste[0])):
             liste[i][j]=chr(liste[i][j])
     return liste




 def transfMatriceAscii(self,liste):
     for i in range(len(liste)):
         for j in range(len(liste[0])):
             liste[i][j]=ord (str(liste[i][j]))
     return liste



    
 def verificationSolution(self,liste):
     solution=1;
     for i in range (len(liste)):
         for j in range(len(liste[0])):
             if(liste[i][j]==48):#/48==nbP):
                 solution=0
     return solution



    
 def sommeListeMatrices(self,listS):
     listSomme=deepcopy(listS[0])#np.matrix(deepcopy(listS[0]))
     for i in range(1,len(listS)):
         for j in range(len(listS[i])):
             for k in range(len(listS[i][j])):
                 if(((listSomme[j][k]>47 )and(listSomme[j][k]<58)) and   ( (listS[i][j][k]>47 )and(listS[i][j][k]<58))  ):
                     if(int(chr(listSomme[j][k]))+int(chr(listS[i][j][k]))>9 ):
                        listSomme[j][k]=listSomme[j][k]
                     else:
                        listSomme[j][k]=ord(str(int(chr(listSomme[j][k]))+int(chr(listS[i][j][k]))))
                 else:
                     if((listS[i][j][k]<48 )or(listS[i][j][k]>57)):
                         listSomme[j][k]=listS[i][j][k]
                     else:
                         listSomme[j][k]=listSomme[j][k]                    
     return listSomme







    
 def grandisMatrices(self):
     
     f=open("entree9.txt", "r")
     x=0
     l2=[]  
     ligne=(f.readline())
     colonne=(f.readline())
     #print ligne,colonne
     L1=int(float(ligne))
     H1=int(float(colonne))
     #print L1,H1
     #initialisation du matrice nomé  piece
     piece=[0]*L1
     for i in range(L1):
         piece[i]=[0]*H1
    
     #lire la ligne 3 qui contient des diéses 
     ch=f.readline()
     #lire la 4 ligne  qui contier de piece 
     ch=f.readline() 

     while (ch[0]!='f'):#remplissage de la liste l2 (une liste de piece )
     
         while ((ch[0] != '#')&(x<ligne))  :#recuperation d'une iece
             for i in range (len(ch)-1):
                 piece[x][i]=(ch[i])
             ch=f.readline()
             #print ch
         
             x=x+1
             #print piece    
         l2.append(piece)
    
         x=0
         ch=f.readline()
         piece=[0]*L1
         for j in range(L1):
             piece[j]=[0]*H1

     return l2






 def rechercherZeroColone(self,M):
     ## M Matrice 
     Zlist=[] # liste contenant le nombre de zero à l'ext de chaque ligne 
     nbZC=0 # nombre de zero par Ligne  
     for i in range(len(M[0])):  
         nbZC=0;
         for j in range(len(M)-1,-1,-1):
             if(M[j][i]==48):
                 nbZC=nbZC+1
             else:
                 Zlist.append(nbZC)
                 break
     Zlist.sort()
     return Zlist[0]







 def rechercherZeroLigne(self,M):
     ## M Matrice 
     Zlist=[] # liste contenant le nombre de zero à l'ext de chaque colonne 
     nbZL=0 # nombre de zero par Colonne  
     for i in range(len(M)):
          
          nbZL=0
          for j in range(len(M[0])-1,-1,-1):
              if (M[i][j]==48):
                  nbZL=nbZL+1

         
              else :
                  Zlist.append(nbZL)
                  break
     Zlist.sort()
     return Zlist[0]










 def afficherUneMatrice(self,A):
     for i in range(0, len(A)):
         print('')
         for j in range(len(A[0])):
             print(A[i][j]),











 def ajouter_deplacement(self,nbrDeplacementL,nbrDeplacementC,matrice):
     m1=matrice[:]
     ttDeplacement=[]
     #print('deplacement vert de cette piece')
     ttDeplacement.append(deepcopy(m1))
     #afficherUneMatrice(matrice)
     #print('')
     self.ajouter_deplacementV(nbrDeplacementL,nbrDeplacementC,deepcopy(m1),ttDeplacement)
     while (nbrDeplacementL>0):
      for i in range(0, len(matrice)):
            for j in range(len(matrice[0])-1,-1,-1):
               m1[i][j]=matrice[i][j-1]#=matrice[i][j]
               if (j==0):
                    m1[i][j]=48
      ttDeplacement.append(deepcopy(m1))
      #print('deplacement vert de cette piece')
      self.ajouter_deplacementV(nbrDeplacementL,nbrDeplacementC,deepcopy(m1),ttDeplacement)
      nbrDeplacementL=nbrDeplacementL-1
     return deepcopy(ttDeplacement)









 def ajouter_deplacementV(self,nbrDeplacementL,nbrDeplacementC,matrice,ttDeplacement):
     m1=matrice
     #afficherUneMatrice(m1)
     while (nbrDeplacementC>0):
      for i in range(0, len(matrice[0])):
            for j in range(len(matrice)-1,-1,-1):
               m1[j][i]=matrice[j-1][i]#=matrice[i][j]
               if (j==0):
                    m1[j][i]=48
      ttDeplacement.append(deepcopy(m1))
      nbrDeplacementC=nbrDeplacementC-1






 def listContainer(self,ttPiece):
     ttDeplacement=[]
     for i in range(len(ttPiece)):
         nbl=self.rechercherZeroLigne(ttPiece[i])
         nbc=self.rechercherZeroColone(ttPiece[i])
         ttDeplacement.append(deepcopy(self.ajouter_deplacement(nbl,nbc,ttPiece[i])))
     return ttDeplacement








Solver= AlgorithmeReso()
Solver.totalListPieceNonAscied=Solver.grandisMatrices()
Solver.totalListPiece=Solver.trasfTTMatAsci(deepcopy(Solver.totalListPieceNonAscied))
Solver.totalPiecesDeplacements=Solver.listContainer(Solver.totalListPiece)
print('Le programme est entrain de calculer toute les combinaisons possibles entres les differentes pieces dans les differentes postions...')
Solver.totalCombinaison=list(itertools.product(*Solver.totalPiecesDeplacements))
print('')
print('')
print('')
print('Le programme est entrain de trouver toute les solutions possibles...')
print('')
print('')
print('')
mon_fichier = open("sortieFinal91.txt", "w")
numS=0
for i in range(len(Solver.totalCombinaison)):
   malistA=Solver.sommeListeMatrices(deepcopy(Solver.totalCombinaison[i]))
   r=Solver.verificationSolution(deepcopy(malistA))
   if(r==1):
       numS=numS+1
       Desc='La solution numero '+str(numS)
       print(Desc)
       matriceSolution=Solver.transfAsciedMat(malistA)
       Solver.afficherUneMatrice(matriceSolution)
       mon_fichier.write("\n")
       mon_fichier.write("\n")
       mon_fichier.write(Desc)
       mon_fichier.write("\n")
       for i in range (len(matriceSolution)):
            mon_fichier.write("\n")
            for j in range (len(matriceSolution[0])):
                mon_fichier.write(matriceSolution[i][j])
                mon_fichier.write(' ')
       print("")
       print("")
mon_fichier.close()
