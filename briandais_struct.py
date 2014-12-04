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

    def accept(self,visitor):
        if self.value == end_of_word :
            visitor.eow(self)
        elif self.child is not None :
            visitor.visit_child(self.child)
            visitor.after_visit_child(self)
        if self.sibling is not None :
            visitor.visit_sibling(self.sibling)
            visitor.after_visit_sibling(self)
            
    def suppress_word(self,word) :
        if len(word) == 0 :
            if self.value == end_of_word :
                return {'found': True, 'suppressed': False}
            elif self.sibling is None :
                return {'found': False, 'suppressed': False}

        elif word[0:1] == self.value :
            if self.child is None :
                return {'found': False, 'suppressed': False}
            else :
                state = self.child.suppress_word(word[1:])
                if state['found'] is True and state['suppressed'] is False :
                    self.child = self.child.sibling
                    if self.child is not None :
                        state['suppressed'] = True
                return state

        elif self.sibling is None :
            return {'found': False, 'suppressed': False}

        
        state = self.sibling.suppress_word(word)
        if state['found'] is True and state['suppressed'] is False :
            self.sibling = self.sibling.sibling
            state['suppressed'] = True
        return state
