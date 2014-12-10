import hybrid_structure
import time
from os import listdir
from os.path import isfile, join

def Exemple_de_Base():
    chaine = "A quel genial professeur de dactylographie sommes nous redevables de la superbe phrase ci dessous, un modele du genre, que tout dactylo connait par coeur puisque elle fait appel a chacune des touches du clavier de la machine a ecrire ?"
    liste = chaine.split(" ")
    while "" in liste : liste.remove("")
    print ("Nombre de mots dans la phrase: "+ str(len(liste)))
    node = hybrid_structure.build_nodes(liste[0])
    for word in liste[1:]:
        node.add_word(word)
    return node



def Recherche(node, word):
    return node.has_word(word)

def ComptageMots(node):
    return node.compte_mots(0)

def ListerMots(arbre):
    liste=ListeUnMot(arbre,"")
    return sorted(liste);

def ListeUnMot(arbre,word):
    liste = []
    if arbre.value == hybrid_structure.end_of_word:
        liste.append(word)

    if arbre.eq is not None:
        liste += ListeUnMot(arbre.eq,word + arbre.value)
        
    if arbre.inf is not None:
        liste += ListeUnMot(arbre.inf,word)

    if arbre.sup is not None:
        liste += ListeUnMot(arbre.sup,word)
    
    return liste


def ComptageNil(arbre):
    cpt = 0

    if arbre.eq is None:
        cpt += 1
    else:   
        cpt += ComptageNil(arbre.eq)

    if arbre.inf is None:
        cpt += 1
    else:
        cpt += ComptageNil(arbre.inf)
    
    if arbre.sup is None:
        cpt += 1
    else:
        cpt += ComptageNil(arbre.sup)

    return cpt

def ComptageNoeuds(arbre):
    nn = 0

    if arbre.eq is not None:
        nn += 1 + ComptageNoeuds(arbre.eq)

    if arbre.inf is not None:
        nn += 1 + ComptageNoeuds(arbre.inf)

    if arbre.sup is not None:
        nn += 1 + ComptageNoeuds(arbre.sup)

    return nn

def Hauteur(arbre):
    h1 = 0
    h2 = 0
    h3 = 0
    if arbre.eq is not None:
        h1 += 1 + Hauteur(arbre.eq)

    if arbre.inf is not None:
        h2 += 1 + Hauteur(arbre.inf)

    if arbre.sup is not None:
        h3 += 1 + Hauteur(arbre.sup)

    return max(h1,h2,h3)

def ProfondeurParNoeud(arbre,n):
    if arbre is None:
        return 0

    return n + ProfondeurParNoeud(arbre.eq,n+1) + ProfondeurParNoeud(arbre.inf,n+1) + ProfondeurParNoeud(arbre.sup,n+1)


def ProfondeurMoyenne(arbre):
    return round(float(ProfondeurParNoeud(arbre,0))/float(ComptageNoeuds(arbre)),3)


def Prefixe(arbre,word):
    return arbre.prefixe(word)

def Supprimer(arbre,word):
    if arbre.has_word(word) is True:
        arbre.del_word(word)


# arbre = Exemple_de_Base()


def Shakespeare():

    path = "./Shakespeare/"
    onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]

    list = []

    for filename in onlyfiles :

        file = open(path+filename,'r')
        string = file.read()

        list += string.split("\n")


    while "" in list : list.remove("")


    ts = time.clock()
    arbre = hybrid_structure.build_nodes(list[0])

    for word in list[1:] :
        arbre.add_word(word)
    te = time.clock()

    print 'Construction de la structure en :',1000*(te - ts),' millisecondes'

    return arbre

#fichier = open("shakespear/fic.txt","r")
#avant = time.clock()
#arbre = hybrid_structure.build_nodes(fichier.readline())
#for ligne in fichier:
#        arbre.add_word(ligne)
#print 'Time execution : ',time.clock() - avant,' secondes\n'

arbre = Shakespeare()

avant = time.clock()
print( "Nombre de mots dans l'arbre: " + str(ComptageMots(arbre)))
print 'Time execution comptage mot : ',time.clock()*1000 - avant*1000,' millisecondes\n'

avant = time.clock()
print( "Nombre de Nil dans l'arbre: " + str(ComptageNil(arbre)) )
print 'Time execution nombre de null: ',time.clock()*1000 - avant*1000,' millisecondes\n'

avant = time.clock()
print( "Nombre de noeuds dans l'arbre: " + str(ComptageNoeuds(arbre)) )
print 'Time execution nombre de noeuds: ',time.clock()*1000 - avant*1000,' millisecondes\n'

avant = time.clock()
print( "Hauteur de l'arbre: " + str(Hauteur(arbre)) )
print 'Time execution hauteur : ',time.clock()*1000 - avant*1000,' millisecondes \n'

avant = time.clock()
print( "Profondeur moyenne de l'arbre: " + str(ProfondeurMoyenne(arbre)) )
print 'Time execution profondeur moyenne: ',time.clock()*1000 - avant*1000,' millisecondes\n'

word = "the"

avant = time.clock()
print( "Occurence prefixe \""+word+"\": " + str(Prefixe(arbre,word )) )
print 'Time execution prefixe: ',time.clock()*1000 - avant*1000,' millisecondes\n'

word = "machinerie"
avant = time.clock()
print( "ajouter un long mot \""+word+"\": " + str(arbre.add_word(word) ))
print 'Time ajouter un mot: ',time.clock()*1000 - avant*1000,' millisecondes\n'

avant = time.clock()
print( "Nombre de mots dans l'arbre: " + str(ComptageMots(arbre)))
print 'Time execution comptage mot : ',time.clock()*1000 - avant*1000,' millisecondes\n'

word = "jessica"
avant = time.clock()
print( "Chercher "+word+" : " + str(arbre.has_word(word)) )
print 'Time execution trouver un mot: ',time.clock()*1000 - avant*1000,' millisecondes\n'

avant = time.clock()
print( "supprimer \""+word+"\": ")
Supprimer(arbre,word)
print 'Time supprimer: ',time.clock()*1000 - avant*1000,' millisecondes\n'

avant = time.clock()
print( "Nombre de mots dans l'arbre: " + str(ComptageMots(arbre)))
print 'Time execution comptage mot : ',time.clock()*1000 - avant*1000,' millisecondes\n'


# print arbre.has_word(word)

# Supprimer(arbre,word)

# print str(arbre.has_word(word))

# print( "Nombre de mots dans l'arbre: " + str(ComptageMots(arbre)))

avant = time.clock()
liste = ListerMots(arbre)
print 'Time Construire liste des mots: ',time.clock()*1000 - avant*1000,' millisecondes\n'
