end_of_word = "\0"

def build_nodes(word):
    if len(word) == 0:
        return Node(end_of_word, None, None, None)
    else:
        return Node(word[0], None, build_nodes(word[1:]), None)

def insert(node,into):
    if node.value == into.value :
        if into.eq is None :
            into.eq = node.eq
        elif node.eq is not None :
            insert(node.eq, into.eq)

    if node.value > into.value :
        if into.sup is None :
            into.sup = node
        else :
            insert(node,into.sup)

    if node.value < into.value :
        if into.inf is None :
            into.inf = node
        else :
            insert(node,into.inf)

def clone(node) :
    if node is None :
        return None
    return Node(node.value, clone(node.inf), clone(node.eq), clone(node.sup))

class Node():

    def __init__(self, value, inf, eq, sup):
        self.value = value
        self.inf = inf
        self.eq = eq
        self.sup = sup

    def has_word(self, word):
        if len(word) == 0:
            if self.value == end_of_word :
                return True
            elif self.inf is not None:
                return self.inf.has_word(word)
            else:
                return False

        elif self.value == word[0]:
            if self.eq is None:
                return False
            else:
                return self.eq.has_word(word[1:])

        elif self.value > word[0]:
            if self.inf is None:
                return False 
            else: 
                return self.inf.has_word(word)

        elif self.value < word[0]:
            if self.sup is None:
                return False 
            else :
                return self.sup.has_word(word)


    def add_word(self,word):
        #print word
        if len(word) == 0:
            if self.value == end_of_word:
                return
            
            # On ne veut jamais ajouter dans self.eq
            # Heuresement il n'est jamais nul si value != EOW
            
            #elif self.eq is None :
            #    self.eq = Node(end_of_word, None, None, None)
            
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

        if len(word) == 0 :
            if self.value == end_of_word : 
                return {'found': True, 'deleted': False}
            elif self.inf is not None :
                state =  self.inf.del_word(word)
                if state['found'] == True and state['deleted'] == False :
                    if self.inf.sup is None and self.inf.inf is None :
                        self.inf = None
                        state['deleted'] = True
                    else :
                        inf = self.inf
                        self.inf = inf.sup
                        if self.inf is None :
                            self.inf = inf.inf
                        elif inf.inf is not None :
                            insert(inf.inf,self.inf)
                        state['deleted'] = True
            else :
                return {'found': False, 'deleted': False}


        elif self.value == word[0]:
            if self.eq is not None:
                state = self.eq.del_word(word[1:])
                if state['found'] == True and state['deleted'] == False :
                    if self.eq.sup is None and self.eq.inf is None :
                        self.eq = None
                    else :
                        eq = self.eq
                        self.eq = eq.sup
                        if self.eq is None :
                            self.eq = eq.inf
                        elif eq.inf is not None :
                            insert(eq.inf,self.eq)
                        
                        if self.eq is not None :
                            state['deleted'] = True
                    
            else:
                return {'found': False, 'deleted': False}

        elif self.value > word[0]:
            if self.inf is not None :
                state = self.inf.del_word(word)
                if state['found'] == True and state['deleted'] == False :
                    if self.inf.sup is None and self.inf.inf is None :
                        self.inf = None
                        state['deleted'] = True
                    else :
                        inf = self.inf
                        self.inf = inf.sup
                        if self.inf is None :
                            self.inf = inf.inf
                        elif inf.inf is not None :
                            insert(inf.inf,self.inf)
                        state['deleted'] = True
            else: 
                return {'found': False, 'deleted': False}

        elif self.value < word[0]:
            if self.sup is not None:
                state = self.sup.del_word(word)
                if state['found'] == True and state['deleted'] == False :
                    if self.sup.sup is None and self.sup.inf is None :
                        self.sup = None
                        state['deleted'] = True
                    else :
                        sup = self.sup
                        self.sup = sup.sup
                        if self.sup is None :
                            self.sup = sup.inf
                        elif sup.inf is not None :
                            insert(sup.inf,self.sup)
                        state['deleted'] = True
            else :
                return {'found': False, 'deleted': False}

        return state

    def prefixe(self, word, total=0):

        if len(word) == 0:
            total += self.compte_mots(0)

        else:
            if word[0] == self.value:
                if self.eq is not None :
                    total += self.eq.prefixe(word[1:],total)
                else:
                    return total

            elif word[0] < self.value:
                if self.inf is not None :
                    total += self.inf.prefixe(word,total)
                else:
                    return total

            elif word[0] > self.value:
                if self.sup is not None:
                    total += self.sup.prefixe(word,total)
                else:
                    return total

        return total

    def print_hybrid_trie(self, depth=0):
        ret = ""

        if self.inf is not None:
            ret += ""+self.inf.print_hybrid_trie(depth + 1)

        if self.eq is not None:
            ret +=  ("*"*(depth-1)) + str(self.value) + self.eq.print_hybrid_trie(depth + 1)
        else:
            ret +=  "\n"+ (""*depth) +str(self.value)

        if self.sup is not None:
            ret += ""+self.sup.print_hybrid_trie(depth + 1)

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
