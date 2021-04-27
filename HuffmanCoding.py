from typing import Any

class HuffmanCoding:
    def rec(self,node,r,val=''):
        
        new_v = val+str(node.code)
        if node.left:
            self.rec(node.left,r,new_v)
        if node.right:
            self.rec(node.right,r,new_v)
        if not node.left and not node.right:
            # print(node.sym,new_v)
            r[node.sym] = new_v
        # print(r)
        return r

    def build(self, text : str) -> Any:
        d = {}
        for i in text:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        nodes = []
        for i in d:
            nodes.append(Node(d[i],i))
        while len(nodes)>1:
            nodes = sorted(nodes, key=lambda x: x.freq)
            l = nodes[0]
            r = nodes[1]
            l.code = '0'
            r.code = '1'

            new_node = Node(l.freq+r.freq,l.sym+r.sym,l,r)
            nodes.remove(l)
            nodes.remove(r)
            nodes.append(new_node)
        y = {}
        d = self.rec(nodes[0],y)
        return d
        # return self.encode(d,text)

    

    def encode(self, Dic : Any, text : str)->str:
        s = ''
        for i in text:
            s += Dic[i]
        print(s)
        return s
    

    def decode(self, Dic : Any, text : str) -> str:
        
        d = {}
        for k, v in Dic.items():
            d[v] = k

        u = ''
        final = ''
        i = 1
        while(len(text)!=0):
            if text[:i] in d.keys():
                final += d[text[:i]]
                text = text[i:]
                i=1
            else:
                i+=1
        return final



class Node:
    def __init__(self,freq,sym,left=None,right=None):
        self.freq = freq
        self.sym = sym
        self.left = left
        self.right = right
        self.code = ''

# print(HuffmanCoding().build("AAAABWWWDD"))
# z = {'A': '0', 'W': '10', 'B': '110', 'D': '111'}
# m = "0000110101010111111"
# print(HuffmanCoding().decode(z,m))
