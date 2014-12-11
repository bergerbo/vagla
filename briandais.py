import briandais_struct
import briandais_visitors
import time
from os import listdir
from os.path import isfile, join

def Recherche(arbre, mot):
    v = briandais_visitors.SearchVisitor(mot)
    v.visit_child(arbre)
    return v.found

def ComptageMots(arbre):
    v =  briandais_visitors.CountVisitor()
    v.visit_child(arbre)
    return v.cpt

def ListeMots(arbre):
    list = arbre.list_words()
    return sorted(list, key=str.lower)

def ComptageNil(arbre):
    v = briandais_visitors.NilVisitor()
    v.visit_child(arbre)
    return v.cpt

def Hauteur(arbre):
    v = briandais_visitors.HeightVisitor()
    v.visit_child(arbre)
    return v.height

def ProfondeurMoyenne(arbre):
    v = briandais_visitors.AverageDepthVisitor()
    v.visit_child(arbre)
    return v.average()

def Prefixe(arbre,mot):
    v = briandais_visitors.PrefixCountVisitor(mot)
    v.visit_child(arbre)
    return v.cpt

def Suppression(arbre, mot):
    arbre.delete_word(mot)

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

cpt = ComptageMots(arbre)
print cpt

liste = ListeMots(arbre)
#print liste

arbre2 = briandais_struct.clone(arbre)

for mot in liste :
    if liste.index(mot) % 2 == 0 :
        Suppression(arbre,mot)
    else :
        Suppression(arbre2,mot)

liste = ListeMots(arbre)
liste2 = ListeMots(arbre2)

#print liste
#print liste2

arbre3 = briandais_struct.fuse_trees(arbre,arbre2)

liste3 = ListeMots(arbre3)
#print liste3



# arbre = Shakespeare()

# avant = time.clock()
# print( "Nombre de mots dans l'arbre: " + str(ComptageMots(arbre)))
# print 'Time execution comptage mot : ',time.clock()*1000 - avant*1000,' millisecondes\n'

# avant = time.clock()
# print( "Nombre de Nil dans l'arbre: " + str(ComptageNil(arbre)) )
# print 'Time execution nombre de null: ',time.clock()*1000 - avant*1000,' millisecondes\n'

# avant = time.clock()
# print( "Hauteur de l'arbre: " + str(Hauteur(arbre)) )
# print 'Time execution hauteur : ',time.clock()*1000 - avant*1000,' millisecondes \n'

# avant = time.clock()
# print( "Profondeur moyenne de l'arbre: " + str(ProfondeurMoyenne(arbre)) )
# print 'Time execution profondeur moyenne: ',time.clock()*1000 - avant*1000,' millisecondes\n'

# word = "frocfjiefiejei"

# avant = time.clock()
# print( "Occurence prefixe \""+word+"\": " + str(Prefixe(arbre,word )) )
# print 'Time execution prefixe: ',time.clock()*1000 - avant*1000,' millisecondes\n'

# word = "machinerie"
# avant = time.clock()
# print( "ajouter un long mot \""+word+"\": " + str(arbre.add_word(word) ))
# print 'Time ajouter un mot: ',time.clock()*1000 - avant*1000,' millisecondes\n'

# avant = time.clock()
# print( "Nombre de mots dans l'arbre: " + str(ComptageMots(arbre)))
# print 'Time execution comptage mot : ',time.clock()*1000 - avant*1000,' millisecondes\n'

# word = "jessica"
# avant = time.clock()
# print( "Chercher "+word+" : " + str(arbre.has_word(word)) )
# print 'Time execution trouver un mot: ',time.clock()*1000 - avant*1000,' millisecondes\n'

# avant = time.clock()
# print( "supprimer \""+word+"\": ")
# Suppression(arbre,word)
# print 'Time supprimer: ',time.clock()*1000 - avant*1000,' millisecondes\n'

# avant = time.clock()
# print( "Nombre de mots dans l'arbre: " + str(ComptageMots(arbre)))
# print 'Time execution comptage mot : ',time.clock()*1000 - avant*1000,' millisecondes\n'


# avant = time.clock()
# liste = ListeMots(arbre)
# print 'Time Construire liste des mots: ',time.clock()*1000 - avant*1000,' millisecondes\n'
# print len(liste)

# avant = time.clock()
# cpt = 0
# for mot in liste :
#     if liste.index(mot) % 2 == 0 :
#         Suppression(arbre,mot)
#         cpt += 1
# print cpt
# print 'Time supprimer la moitier des mots: ',time.clock()*1000 - avant*1000,' millisecondes\n'
# print( "Nombre de mots dans l'arbre: " + str(ComptageMots(arbre)))
