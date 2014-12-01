import briandais_struct
import briandais_visitors

def Recherche(arbre, mot):
    v = briandais_visitors.SearchVisitor(mot)
    v.visit_child(arbre)
    return v.found

def ComptageMots(arbre):
    v =  briandais_visitors.CountVisitor()
    v.visit_child(arbre)
    return v.cpt

def ListeMots(arbre):
    v = briandais_visitors.ListVisitor()
    v.visit_child(arbre)
    return sorted(v.list, key=str.lower)

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
    v = briandais_visitors.SuppressVisitor(mot)
    v.visit_child(arbre)

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

arbre = ExampleBase()
liste = ListeMots(arbre)
nbMots = ComptageMots(arbre)
nbNil = ComptageNil(arbre)
hauteur = Hauteur(arbre)
profMoyenne = ProfondeurMoyenne(arbre)
prefixeDactylo = Prefixe(arbre,"dactylo")
echecRecherche = Recherche(arbre,"Malkovich")
rechercheGenerale = True
for mot in liste :
    rw = Recherche(arbre,mot)
    rechercheGenerale = rechercheGenerale and rw

print liste
print echecRecherche
print rechercheGenerale
print nbMots
print nbNil
print hauteur
print profMoyenne
print prefixeDactylo

#for mot in liste :
#    if liste.index(mot) % 2 == 0 :
#        print mot
#           Suppression(arbre,mot)
Suppression(arbre,"modele")
Suppression(arbre,"dactylographie")

liste = ListeMots(arbre)
nbMots = ComptageMots(arbre)
nbNil = ComptageNil(arbre)
hauteur = Hauteur(arbre)
profMoyenne = ProfondeurMoyenne(arbre)
prefixeDactylo = Prefixe(arbre,"dactylo")
echecRecherche = Recherche(arbre,"Malkovich")
rechercheGenerale = True
for mot in liste :
    rw = Recherche(arbre,mot)
    rechercheGenerale = rechercheGenerale and rw

print liste
print echecRecherche
print rechercheGenerale
print nbMots
print nbNil
print hauteur
print profMoyenne
print prefixeDactylo
