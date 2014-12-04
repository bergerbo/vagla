import hybrid_structure

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
    tmp=[]
    liste=ListeUnMot(arbre,"",tmp)
    return sorted(liste);

def ListeUnMot(arbre,word,liste):

    if arbre.value == hybrid_structure.end_of_word:
        #print word
        if arbre.inf is not None:
            ListeUnMot(arbre.inf,word,liste)
        if arbre.sup is not None:
            ListeUnMot(arbre.sup,word,liste)
        liste.append(word)

    if arbre.eq is not None:
        word += arbre.value
        ListeUnMot(arbre.eq,word,liste)
        
    if arbre.inf is not None:
        ListeUnMot(arbre.inf,word[0:-1],liste)

    if arbre.sup is not None:
        ListeUnMot(arbre.sup,word[0:-1],liste)
    
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


def OccurenceMot(arbre, word):
    taille = len(word)




arbre = Exemple_de_Base()

print arbre.has_word("quel")

print( "Nombre de mots dans l'arbre: " + str(ComptageMots(arbre)))

print( "Nombre de Nil dans l'arbre: " + str(ComptageNil(arbre)) )

print( "Nombre de noeuds dans l'arbre: " + str(ComptageNoeuds(arbre)) )

print( "Hauteur de l'arbre: " + str(Hauteur(arbre)) )

print( "ProfondeurParNoeud: " + str(ProfondeurParNoeud(arbre,0)) )

print( "Profondeur moyenne de l'arbre: " + str(ProfondeurMoyenne(arbre)) )

liste = ListerMots(arbre)
#print liste
#for word in liste[0:]:
 #   print word


print arbre.print_hybrid_trie()
