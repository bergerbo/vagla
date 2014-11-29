end_of_word = "\0" 

def build_nodes(word):
    if len(word) == 0 :
        return Node(end_of_word, None, None)

    else:
        return Node(word[0], None, build_nodes(word[1:]))

class Node():

    def __init__(self, value, sibling, child):
        self.value = value
        self.sibling = sibling
        self.child = child

    def add_word(self,word):
        if len(word) == 0 :
            if self.value == end_of_word :
                return
            elif self.sibling is None :
                self.sibling = Node(end_of_word, self.sibling, None)
            else :
                self.sibling.add_word(word)

        elif word[0] == self.value :
            if self.child is None :
                self.child = build_nodes(word)
            else :
                self.child.add_word(word[1:])

        elif self.sibling is None :
            self.sibling = Node(word[0], None, build_nodes(word[1:]))

        else :
            self.sibling.add_word(word)

    def accept(self,visitor):
        if self.value == end_of_word :
            visitor.eow(self)
        elif self.child is not None :
            visitor.visit_child(self.child)
        if self.sibling is not None :
            visitor.visit_sibling(self.sibling)

    def has_word(self, word):
        if len(word) == 0 :
            if self.value == end_of_word :
                return True
            else :
                return self.sibling_has_word(word)

        elif word[0] == self.value :
            return self.child.has_word(word[1:])

        else :
            return self.sibling_has_word(word)


    def sibling_has_word(self,word):
        if self.sibling is None :
            return False
        else : 
            return self.sibling.has_word(word)	


    def get_words(self, list, prefix):
        if self.value == end_of_word :
            list.append(prefix)
        elif self.child is not None :
            self.child.get_words(list, prefix + self.value)
        if self.sibling is not None :
            self.sibling.get_words(list, prefix)

    def count_words(self, cpt) :
        ncpt = 0
        if self.value == end_of_word :
            ncpt = 1
        elif self.child is not None :
            ncpt = self.child.count_words(cpt)

        if self.sibling is not None :
            return self.sibling.count_words(0) + ncpt
        else :
            return ncpt

class Visitor():

    def eow(self,node):
        return

    def visit_child(self,node):
        node.accept(self)

    def visit_sibling(self,node):
        node.accept(self)


class CountVisitor(Visitor):
    def __init__(self):
        self.cpt = 0

    def eow(self,node):
        self.cpt += 1


class PrefixVisitor(Visitor):
    def __init__(self):
        self.prefix = ""

    def visit_child(self,node):
        self.prefix = self.prefix + node.value
        node.accept(self)
        self.prefix = self.prefix[:-1]

    def visit_sibling(self,node):
        self.prefix = self.prefix[:-1] + node.value
        node.accept(self)

class MatchingVisitor(PrefixVisitor):
    def __init__(self,word):
        PrefixVisitor.__init__(self)
        self.word = word

    def visit_child(self, node):
        l = min(len(self.prefix),len(self.word))
        if self.word[:l] == self.prefix[:l] :
            PrefixVisitor.visit_child(self,node)

class SearchVisitor(MatchingVisitor):
    def __init__(self,word):
        MatchingVisitor.__init__(self,word)
        self.found = False

    def eow(self,node):
        if self.word == self.prefix[:-1] :
            self.found = True

class PrefixCountVisitor(MatchingVisitor):
    def __init__(self,word):
        MatchingVisitor.__init__(self,word)
        self.cpt = 0

    def eow(self, node):
        self.cpt += 1

class SupressVisitor(MatchingVisitor):
    def __init__(self,word):
        MatchingVisitor.__init__(self,word)
        

class ListVisitor(PrefixVisitor):
    def __init__(self):
        PrefixVisitor.__init__(self)
        self.list = []

    def eow(self,node):
        self.list.append(self.prefix[:-1])

class NilVisitor(Visitor):
    def __init__(self):
        self.cpt = 0

    def count(self, node):
        if node.child is None :
            self.cpt += 1
        if node.sibling is None :
            self.cpt +=1

    def visit_child(self,node):
        self.count(node)
        node.accept(self)

    def visit_sibling(self,node):
        self.count(node)
        node.accept(self)


class HeightVisitor(Visitor):
    def __init__(self) :
        self.depth = 0
        self.height = 0

    def visit_child(self,node):
        self.depth += 1
        if self.depth > self.height :
            self.height = self.depth
        node.accept(self)
        self.depth -= 1

class AverageDepthVisitor(Visitor):
    def __init__(self) :
        self.depth = 0
        self.cpt = 0
        self.total = 0

    def handle(self, node) :
        self.total += self.depth
        self.cpt += 1

    def average(self):
        return self.total / float(self.cpt)

    def visit_child(self,node):
        self.depth += 1
        self.handle(node)
        node.accept(self)
        self.depth -= 1

    def visit_sibling(self,node):
        self.handle(node)
        node.accept(self)

def Recherche(arbre, mot):
    v = SearchVisitor(mot)
    v.visit_child(arbre)
    return v.found

def ComptageMots(arbre):
    v = CountVisitor()
    v.visit_child(arbre)
    return v.cpt

def ListeMots(arbre):
    v = ListVisitor()
    v.visit_child(arbre)
    return sorted(v.list, key=str.lower)

def ComptageNil(arbre):
    v = NilVisitor()
    v.visit_child(arbre)
    return v.cpt

def Hauteur(arbre):
    v = HeightVisitor()
    v.visit_child(arbre)
    return v.height

def ProfondeurMoyenne(arbre):
    v = AverageDepthVisitor()
    v.visit_child(arbre)
    return v.average()

def Prefixe(arbre,mot):
    v = PrefixCountVisitor(mot)
    v.visit_child(arbre)
    return v.cpt

def ExampleBase():
    example_base = """A quel genial professeur de dactylographie sommes nous
    redevables de la superbe phrase ci dessous, un modele du genre, que tout
    dactylo connait par coeur puisque elle fait appel a chacune des touches du
    clavier de la machine a ecrire?"""
    list = example_base.replace("\n","").split(" ")
    while "" in list : list.remove("")
    node = build_nodes(list[0])
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
