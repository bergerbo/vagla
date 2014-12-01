end_of_word = "\0"

def build_nodes(word):
    if len(word) == 0:
        return Node(end_of_word, None, None, None)
    else:
        return Node(word[0], None, build_nodes(word[1:]), None)


class Node():

    def __init__(self, value, inf, eq, sup):
        self.value = value
        self.inf = inf
        self.eq = eq
        self.sup = sup

    def has_word(self, word):
        if len(word) == 0 :
            if self.value == end_of_word :
                return True

        elif self.value == word[0]:
            self.eq.has_word(word[1:])

        elif self.value > word[0]:
            if self.inf is None :
                return False 
            else: 
                self.inf.has_word(word)

        elif self.value < word[0]:
            if self.sup is None:
                return False 
            else :
                self.sup.has_word(word)

    def add_word(self,word):
        #print word
        if len(word) == 0:
            if self.value == end_of_word:
                return
            elif self.eq is None :
                self.eq = Node(end_of_word, None, None, None)
            elif self.inf is None:
                self.inf = Node(end_of_word, None, None, None)
            else:
                self.inf.add_word(word)
            

        elif word[0] == self.value:
            if self.eq is not None:
                self.eq.add_word(word[1:])
            else:
                self.eq.build_nodes(word[1:])

        elif word[0] < self.value:
            if self.inf is None :
                self.inf = build_nodes(word)
            else :
                self.inf.add_word(word) 
            
        elif word[0] > self.value:
            if self.sup is None:
                self.sup = build_nodes(word)
            else:
                self.sup.add_word(word)


    def del_word(self,word):
        if has_word(word) == False:
            return


    def print_hybrid_trie(self, depth=0):
        ret = ""

        if self.inf is not None:
            ret += self.inf.print_hybrid_trie(depth + 1)

        if self.eq is not None:
            ret += ("-"*depth)+ str(self.value) + self.eq.print_hybrid_trie(depth + 1)
        else:
            ret +=  str(self.value) +"\n"

        if self.sup is not None:
            ret += self.sup.print_hybrid_trie(depth + 1)

        return ret


    def compte_mots(self, n):
        cpt = 0
        if self.value == end_of_word:
            cpt+=1

        if self.eq is not None :
            cpt += self.eq.compte_mots(cpt)

        if self.inf is not None:
            cpt += self.inf.compte_mots(cpt)
        
        if self.sup is not None:
            cpt += self.sup.compte_mots(cpt)

        return cpt
            
        


def Exemple_de_Base():
    chaine = "A quel genial professeur de dactylographie sommes nous redevables de la superbe phrase ci dessous, un modele du genre, que tout dactylo connait par coeur puisque elle fait appel a chacune des touches du clavier de la machine a ecrire ?"
    liste = chaine.split(" ")
    while "" in liste : liste.remove("")
    print ("Nombre de mots dans la phrase: "+ str(len(liste)))
    node = build_nodes(liste[0])
    for word in liste[1:]:
        node.add_word(word)
    return node



def Recherche(node, word):
    return node.has_word(word)

def ComptageMots(node):
    return node.compte_mots(0)

#def ListeMots(node):

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

def ProfondeurMoyenne(arbre):
    

arbre = Exemple_de_Base()
print( "Nombre de mots dans l'arbre: " + str(ComptageMots(arbre)))

print( "Nombre de Nil dans l'arbre: " + str(ComptageNil(arbre)) )

print( "Nombre de noeuds dans l'arbre: " + str(ComptageNoeuds(arbre)) )

print( "Hauteur de l'arbre: " + str(Hauteur(arbre)) )
print arbre.print_hybrid_trie()