import briandais_struct
import hybrid_structure


def TransformeBriandaisEnHybride(briandais):
    return briandais_to_hybrid(briandais,True)

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
            else :
                add_sibling_into_hybrid(node.eq,sibling.child)
                
    elif sibling.value < node.value :
        if node.inf is None :
            node.inf = briandais_to_hybrid(sibling,False)
        else :
            add_sibling_into_hybrid(node.inf,sibling)
    
    elif sibling.value > node.value :
        if node.sup is None :
            node.sup = briandais_to_hybrid(sibling,False)
        else :
            add_sibling_into_hybrid(node.sup,sibling)
            

def TransformeHybrideEnBriandais(hybrid) :
    return hybrid_to_briandais(hybrid)

       
def hybrid_to_briandais(hy) :

    node = briandais_struct.Node(hy.value, None, None)
    
    if hy.eq is not None :
        node.child = hybrid_to_briandais(hy.eq)
            
    chain1 = None
    chain2 = None
    
    if hy.inf is not None :    
        chain1 = hybrid_to_briandais(hy.inf)
    
    if hy.sup is not None :
        chain2 = hybrid_to_briandais(hy.sup)
    
    if chain1 is not None :
        node.sibling = chain1

    temp_node = node
    while temp_node.sibling is not None :
        temp_node = temp_node.sibling
        
    if chain2 is not None :
        temp_node.sibling = chain2
        
    return node