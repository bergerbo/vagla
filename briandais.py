end_of_word = " " 

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


    def add_word(self,word):
        if len(word) == 0 :
            self.sibling = Node(end_of_word, self.sibling, None)

        elif word[0] == self.value :
            if self.child is None :
                self.child = build_nodes(word)
            else :
                self.child.add_word(word[1:])

        elif self.sibling is None :
            self.sibling = Node(word[0], None, build_nodes(word[1:]))

        else :
            self.sibling.add_word(word)

    def print_tree(self, prefix):
        if self.value == end_of_word :
            print repr(prefix)
            #print "\n"
        elif self.child is not None :
            self.child.print_tree(prefix + self.value)
        if self.sibling is not None :
            self.sibling.print_tree(prefix)
    
    def count_words(self, cpt) :
        ncpt = cpt
        if self.value == end_of_word :
            ncpt += 1
        elif self.child is not None :
            ncpt += self.child.count_words(cpt)
        if self.sibling is not None :
            return self.sibling.count_words(ncpt)
        else :
            return ncpt


def Recherche(node, word):
    return node.has_word(word)

def ComptageMots(node):
    return node.count(0)

def ExampleBase():
    example_base = """A quel genial professeur de dactylographie sommes nous
    redevables de la superbe phrase ci dessous, un
    modele du genre, que toute dactylo connait par coeur puisque elle fait appel
    a chacune des touches du
    clavier de la machine a ecrire?"""
    list = example_base.split(" ")
    node = build_nodes(list[0])
    for word in list[1:] :
        node.add_word(word)
    return node
