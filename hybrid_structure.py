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
        if len(word) == 0:
            if self.value == end_of_word :
                print True
                return True
            elif self.inf is not None:
                if self.inf.value == end_of_word:
                    print True
                    return True
                else:
                    print False
                    return False
            else:
                print False
                return False

        elif self.value == word[0]:
            self.eq.has_word(word[1:])

        elif self.value > word[0]:
            if self.inf is None :
                print False
                return False 
            else: 
                self.inf.has_word(word)

        elif self.value < word[0]:
            if self.sup is None:
                print False
                return False 
            else :
                self.sup.has_word(word)

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
        if has_word(word) == False:
            return





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
            