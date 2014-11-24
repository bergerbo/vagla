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
