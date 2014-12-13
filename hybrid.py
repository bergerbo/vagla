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

def ListeMots(arbre):
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


def ComptageNils(arbre):
    cpt = 0

    if arbre.eq is None:
        cpt += 1
    else:   
        cpt += ComptageNils(arbre.eq)

    if arbre.inf is None:
        cpt += 1
    else:
        cpt += ComptageNils(arbre.inf)
    
    if arbre.sup is None:
        cpt += 1
    else:
        cpt += ComptageNils(arbre.sup)

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
        h1 = 1 + Hauteur(arbre.eq)

    if arbre.inf is not None:
        h2 = 1 + Hauteur(arbre.inf)

    if arbre.sup is not None:
        h3 = 1 + Hauteur(arbre.sup)

    return max(h1,h2,h3)

def ProfondeurParNoeud(arbre,n):
    if arbre is None:
        return 0

    return n + ProfondeurParNoeud(arbre.eq,n+1) + ProfondeurParNoeud(arbre.inf,n+1) + ProfondeurParNoeud(arbre.sup,n+1)


def ProfondeurMoyenne(arbre):
    return round(float(ProfondeurParNoeud(arbre,0))/float(ComptageNoeuds(arbre)),3)


def Prefixe(arbre,word):
    return arbre.prefixe(word)

def Suppression(arbre,word):
    arbre.del_word(word)

def Equilibre(arbre):

    if arbre.inf is not None:
        h1 = Hauteur(arbre.inf)
    else:
        h1 = 0

    if arbre.sup is not None:
        h2 = Hauteur(arbre.sup)
    else:
        h2 = 0

    print 'h1 : ',h1
    print 'h2 : ',h2

    if h1 <= 1 and h2 <= 1:
        return arbre

    if h1>h2:
        pivot = arbre.inf
        pivot.sup = arbre
        if arbre.inf.sup is not None:
            pivot.sup.inf = arbre.inf.sup
        else:
            pivot.sup.inf = None
        arbre = pivot
        

    if h2>h1:
        pivot = arbre.sup
        pivot.inf = arbre
        if arbre.sup.inf is not None:
            pivot.inf.sup = arbre.sup.inf
        else:
            pivot.inf.sup = None
        arbre = pivot
    
    if arbre.inf is not None:
        arbre.inf = Equilibre(arbre.inf)
    if arbre.sup is not None:
        arbre.sup = Equilibre(arbre.sup)
    return arbre



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



print '------  Tries Hybrides  -------'
# arbre = Shakespeare()

# ts = time.clock()
# cpt = ComptageMots(arbre)
# te = time.clock()
# print 'Nombre de mots : ',cpt
# print 'Comptage Mots en :',1000*(te - ts),' milliseconds'

# ts = time.clock()
# cptn = ComptageNils(arbre)
# te = time.clock()
# print 'Nombre de Nils : ',cptn
# print 'Comptage Nils en :',1000*(te - ts),' milliseconds'

# ts = time.clock()
# h = Hauteur(arbre)
# te = time.clock()
# print 'Hauteur : ',h
# print 'Hauteur en :',1000*(te - ts),' milliseconds'

# ts = time.clock()
# pm = ProfondeurMoyenne(arbre)
# te = time.clock()
# print 'Profondeur Moyenne : ',pm
# print 'Profondeur moyenne en :',1000*(te - ts),' milliseconds'

# ts = time.clock()
# th = Prefixe(arbre,"the")
# te = time.clock()
# print 'Prefixe the apparait : ',th
# print 'Prefixe the en :',1000*(te - ts),' milliseconds'

# ts = time.clock()
# liste = ListeMots(arbre)
# te = time.clock()
# print 'Liste en :',1000*(te - ts),' milliseconds'

# ts = time.clock()
# arbre2 = hybrid_structure.clone(arbre)
# te = time.clock()
# print 'Clonage en :',1000*(te - ts),' milliseconds'

# ts = time.clock()
# for mot in liste :
#     if liste.index(mot) % 2 == 0 :
#         Suppression(arbre,mot)
#     else :
#         Suppression(arbre2,mot)

# te = time.clock()
# print 'Suppression massive en :',1000*(te - ts),' milliseconds'
# print 'Nombre de mots arbre : ',str(ComptageMots(arbre))
# print 'Nombre de mots arbre 2 : ',str(ComptageMots(arbre2))

arbre = Exemple_de_Base()

print Hauteur(arbre)