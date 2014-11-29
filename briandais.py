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


class CountVisitor():
    def __init__(self):
        self.cpt = 0

    def eow(self,node):
        self.cpt += 1

    def visit_child(self,node):
        node.accept(self)

    def visit_sibling(self,node):
        node.accept(self)

class PrefixVisitor():
    def __init__(self):
        self.prefix = ""

    def eow(self,node):
        return

    def visit_child(self,node):
        self.prefix = self.prefix + node.value
        node.accept(self)
        self.prefix = self.prefix[:-1]

    def visit_sibling(self,node):
        self.prefix = self.prefix[:-1] + node.value
        node.accept(self)

class SearchVisitor(PrefixVisitor):
    def __init__(self,word):
        PrefixVisitor.__init__(self)
        self.word = word
        self.found = False

    def eow(self,node):
        if self.word == self.prefix[:-1] :
            self.found = True

class ListVisitor(PrefixVisitor):
    def __init__(self):
        PrefixVisitor.__init__(self)
        self.list = []

    def eow(self,node):
        self.list.append(self.prefix[:-1])


def Recherche(node, word):
    v = SearchVisitor(word)
    v.visit_child(node)
    return v.found

def ComptageMots(node):
    v = CountVisitor()
    v.visit_child(node)
    return v.cpt

def ListeMots(node):
    v = ListVisitor()
    v.visit_child(node)
    return sorted(v.list, key=str.lower)

def ExampleBase():
    example_base = """A quel genial professeur de dactylographie sommes nous
    redevables de la superbe phrase ci dessous, un modele du genre, que tout
    dactylo connait par coeur puisque elle fait appel a chacune des touches du
    clavier de la machine a ecrire?"""
    list = example_base.replace("\n","").split(" ")
    node = build_nodes(list[0])
    for word in list[1:] :
        node.add_word(word)
    return node



x = ExampleBase()
l = ListeMots(x)
nb = ComptageMots(x)

r = True
for word in l :
    rw = Recherche(x,word)
    if rw == False :
        r = False

print l
print r
print nb
