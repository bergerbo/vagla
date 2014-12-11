import briandais_struct
import briandais_visitors
import time
from os import listdir
from os.path import isfile, join

def Recherche(arbre, mot):
    return arbre.has_word(mot)

def ComptageMots(arbre):
    return arbre.cpt_words()

def ListeMots(arbre):
    list = arbre.list_words()
    return sorted(list, key=str.lower)

def ComptageNils(arbre):
    return arbre.cpt_nils()

def Hauteur(arbre):
    return arbre.height()


def ProfondeurMoyenne(arbre):
    data = arbre.avg_depth()
    return data['sum'] / (float)(data['cpt'])

def Prefixe(arbre,mot):
    return arbre.cpt_prefix(mot)

def Suppression(arbre, mot):
    arbre.suppress_word(mot)

def ExampleBase():
    example_base = """A quel genial professeur de dactylographie sommes nous
    redevables de la superbe phrase ci dessous, un modele du genre, que tout
    dactylo connait par coeur puisque elle fait appel a chacune des touches du
    clavier de la machine a ecrire ?"""
    list = example_base.replace("\n","").split(" ")
    while "" in list : list.remove("")
    node = briandais_struct.build_nodes(list[0])
    for word in list[1:] :
        node.add_word(word)
    return node

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
    arbre = briandais_struct.build_nodes(list[0])

    for word in list[1:] :
        arbre.add_word(word)

    te = time.clock()
    print 'Construction de la structure en :',1000*(te - ts),' milliseconds'

    return arbre

arbre = Shakespeare()

ts = time.clock()
cpt = ComptageMots(arbre)
te = time.clock()
print cpt
print 'Comptage Mots en :',1000*(te - ts),' milliseconds'

ts = time.clock()
cptn = ComptageNils(arbre)
te = time.clock()
print cptn
print 'Comptage Nils en :',1000*(te - ts),' milliseconds'

ts = time.clock()
h = Hauteur(arbre)
te = time.clock()
print h
print 'Hauteur en :',1000*(te - ts),' milliseconds'

ts = time.clock()
pm = ProfondeurMoyenne(arbre)
te = time.clock()
print pm
print 'Profondeur moyenne en :',1000*(te - ts),' milliseconds'

ts = time.clock()
th = Prefixe(arbre,"the")
te = time.clock()
print th
print 'Prefixe the en :',1000*(te - ts),' milliseconds'

ts = time.clock()
liste = ListeMots(arbre)
te = time.clock()
print 'Liste en :',1000*(te - ts),' milliseconds'

ts = time.clock()
arbre2 = briandais_struct.clone(arbre)
te = time.clock()
print 'Clonage en :',1000*(te - ts),' milliseconds'

ts = time.clock()
for mot in liste :
    if liste.index(mot) % 2 == 0 :
        Suppression(arbre,mot)
    else :
        Suppression(arbre2,mot)

te = time.clock()
print 'Suppression massive en :',1000*(te - ts),' milliseconds'

liste = ListeMots(arbre)
liste2 = ListeMots(arbre2)

#print liste
#print liste2

ts = time.clock()
arbre3 = briandais_struct.fuse_trees(arbre,arbre2)
te = time.clock()
print 'Fusion en :',1000*(te - ts),' milliseconds'

liste3 = ListeMots(arbre3)
#print liste3
