end_of_word = "\0" 

def build_nodes(word):
    if len(word) == 0 :
        return Node(end_of_word, None, None)

    else:
        return Node(word[0], None, build_nodes(word[1:]))

def clone(node) :
    if node is None :
        return None
    return Node(node.value, clone(node.sibling), clone(node.child))

def fuse_trees(node, into):
    value = into.value
    child = None
    sibling = None

    if node.value == into.value :
        if node.child is not None :
            if into.child is not None :
                child = fuse_trees(node.child, into.child)
            else :
                child = clone(node.child)
        else :
            child = clone(into.child)


        if node.sibling is not None :
            if into.sibling is not None :
                sibling = fuse_trees(node.sibling,into.sibling)
            else :
                sibling = clone(node.sibling)
        else :
            sibling = clone(into.sibling)

    else :
        child = clone(into.child)
        if into.sibling is not None :
            sibling = fuse_trees(node,into.sibling)
        else :
            sibling = clone(node);

    return Node(value,sibling,child)

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

    def has_word(self, word):
        if len(word) == 0 :
            if self.value == end_of_word :
                return True

        elif word[0] == self.value :
            if self.child is not None :
                return self.child.has_word(word[1:])
            return False

        if self.sibling is not None :
            return self.sibling.has_word(word)

        return False


    def list_words(self, prefix = ""):
        list = []

        if self.value == end_of_word :
            list.append(prefix)

        if self.child is not None :
            list += self.child.list_words(prefix + self.value)

        if self.sibling is not None :
            list += self.sibling.list_words(prefix)

        return list

    def accept(self,visitor):
        
        if self.value == end_of_word :
            visitor.eow(self)
        
        elif self.child is not None :
            visitor.visit_child(self.child)
            visitor.after_visit_child(self)
        
        if self.sibling is not None :
            visitor.visit_sibling(self.sibling)
            visitor.after_visit_sibling(self)

    def delete_word(self,word) :

        if len(word) == 0 :
            if self.value == end_of_word :
                return {'found': True, 'deleted': False}
            elif self.sibling is None :
                return {'found': False, 'deleted': False}

        elif word[0:1] == self.value :
            if self.child is None :
                return {'found': False, 'deleted': False}
            else :
                state = self.child.delete_word(word[1:])
                if state['found'] is True and state['deleted'] is False :
                    self.child = self.child.sibling
                    if self.child is not None :
                        state['deleted'] = True
                return state

        elif self.sibling is None :
            return {'found': False, 'deleted': False}

        state = self.sibling.delete_word(word)
        if state['found'] is True and state['deleted'] is False :
            self.sibling = self.sibling.sibling
            state['deleted'] = True
        return state
