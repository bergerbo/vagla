import briandais_struct
import hybrid_structure


def briandais_to_hybrid(bri,with_siblings):
    
    node = hybrid_structure.Node(bri.value,None,None,None)
    
    if bri.child is not None :
        node.eq = briandais_to_hybrid(bri.child,True)
    
    if with_siblings is True :
        sibling = bri.sibling
        while sibling is not None :
            add_sibling_into_hybrid(node,sibling)
            sibling = sibling.sibling
    
    return node


def add_sibling_into_hybrid(node,sibling) :
    
    if sibling.value == node.value :
        if sibling.child is not None :
            if node.eq is None :
                node.eq = briandais_to_hybrid(sibling.child,True)
            else
                add_sibling_into_hybrid(node.eq,sibling.child)
                
    elif sibling.value < node.value :
        if node.inf is None :
            node.inf = briandais_to_hybrid(sibling,False)
        else 
            add_sibling_into_hybrid(node.inf,sibling)
    
    elif sibling.value > node.value :
        if node.sup is None :
            node.sup = briandais_to_hybrid(sibling,False)
        else
            add_sibling_into_hybrid(node.sup,sibling)
            