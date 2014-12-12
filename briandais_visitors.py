class Visitor():

    def visit(self,node):
        if node.value == end_of_word :
            self.eow(node)

        elif node.child is not None :
            self.visit_child(node)

        if node.sibling is not None :
            self._visit_sibling(node)

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
        if self.word[l-1:l] == self.prefix[l-1:l] :
            PrefixVisitor.visit_child(self,node)

class SearchVisitor(MatchingVisitor):
    def __init__(self,word):
        MatchingVisitor.__init__(self,word)
        self.found = False

    def eow(self,node):
        if self.word[-1:] == self.prefix[-2:-1] :
            self.found = True

class PrefixCountVisitor(MatchingVisitor):
    def __init__(self,word):
        MatchingVisitor.__init__(self,word)
        self.cpt = 0

    def eow(self, node):
        self.cpt += 1

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
            self.cpt += 1

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
