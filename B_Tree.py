from PIL import Image
import os
import re
import time

class Node:
    def __init__(self, folha = False):
        self.address = []
        self.children = []
        self.folha = folha

class B_Tree:
    def __init__(self, t):
        self.root = Node(True)
        self.t = t

    def split_children(self, x, i):
        t = self.t
        y = x.children[i]
        z = Node(y.folha)

        x.children.insert(i+1, z)
        x.address.insert(i, y.address[t - 1])

        z.address = y.address[t : (2*t)-1]
        y.address = y.address[0 : t-1]

        if not y.folha:
            z.children.extend(y.children[t : 2*t])
            y.children = y.children[:t]
        
    def insert_non_full(self, x, k):
        t = self.t
        i = len(x.address) - 1

        if x.folha:
            x.address.append(None)
            while i >= 0 and k < x.address[i]:
                x.address[i + 1] = x.address[i]
                i-=1
                
            x.address[i + 1] = k

        else:
            while i>= 0 and k < x.address[i]:
                i-=1
            i += 1
            if len(x.children[i].address) == (2*t)-1:
                self.split_children(x, i)

                if i < len(x.address) and k > x.address[i]:
                    i += 1

            self.insert_non_full(x.children[i], k)

    def insert(self, k):
        t = self.t
        root = self.root

        if len(root.address) == (2*t) - 1:
            new = Node()
            self.root = new
            new.children.insert(0, root)
            self.split_children(new, 0)
            self.insert_non_full(new, k)

        else:
            self.insert_non_full(root, k)

    def search(self, key, root = None):
        root = self.root if root == None else root
        images = []

        for addrs in root.address:
            if addrs.startswith(key):
                images.append(addrs)
        
        if root.folha:
            return images
        else:
            for filho in root.children:
                images.extend(self.search(key, filho))

        images.sort()

        return images

    def print_tree(self, x, level=0):
        if len(x.address) > 0:
            print(f'Level {level}: ', end="")

            for key in x.address:
                print(key, end=" ")
                
            print()

        level += 1
        for filho in x.children:
            self.print_tree(filho, level)

    def print_inOrder(self, x):
        i = 0
        result = []

        while i < len(x.address):
            if len(x.children) > i and x.address[i] != None:
                result.extend(self.print_inOrder(x.children[i]))

            result.append(str(x.address[i]))
            
            i += 1

        if len(x.children) > i:
            result.extend(self.print_inOrder(x.children[i]))

        return result
    

    def delete(self, x, k):
        t = self.t
        i = 0
        
        x.address = [addr for addr in x.address if addr is not None]
        
        while i < len(x.address) and k > x.address[i]:
            i += 1

        if x.folha:
            if i < len(x.address) and x.address[i] == k:
                x.address.pop(i)
            return

        if i < len(x.address) and x.address[i] == k:
            return self.delete_internal_node(x, k, i)
        
        if i >= len(x.children):
            return
            
        if len(x.children[i].address) >= t:
            self.delete(x.children[i], k)
        else:
            if i > 0 and len(x.children[i - 1].address) >= t:
                self.delete_sibling(x, i, i - 1)
            elif i < len(x.children) - 1 and len(x.children[i + 1].address) >= t:
                self.delete_sibling(x, i, i + 1)
            else:
                if i > 0:
                    self.delete_merge(x, i - 1, i)
                    i = i - 1
                elif i < len(x.children) - 1:
                    self.delete_merge(x, i, i + 1)
            
            if i < len(x.children):
                self.delete(x.children[i], k)

    def delete_internal_node(self, x, k, i):
        t = self.t
        if x.folha:
            if x.address[i] == k:
                x.address.pop(i)
            return

        if len(x.children[i].address) >= t:
            x.address[i] = self.delete_predecessor(x.children[i])
            return
        elif len(x.children[i + 1].address) >= t:
            x.address[i] = self.delete_successor(x.children[i + 1])
            return
        else:
            self.delete_merge(x, i, i + 1)
            self.delete_internal_node(x.children[i], k, self.t - 1)

    def delete_predecessor(self, x):
        if x.folha:
            return x.address.pop()
        n = len(x.address) - 1
        if len(x.children[n].address) >= self.t:
            self.delete_sibling(x, n + 1, n)
        else:
            self.delete_merge(x, n, n + 1)
        self.delete_predecessor(x.children[n])

    def delete_successor(self, x):
        if x.folha:
            return x.address.pop(0)
        if len(x.children[1].address) >= self.t:
            self.delete_sibling(x, 0, 1)
        else:
            self.delete_merge(x, 0, 1)
        self.delete_successor(x.children[0])

    def delete_merge(self, x, i, j):
        if i >= len(x.children) or j >= len(x.children):
            return
            
        cnode = x.children[i]
        
        if j > i:
            if j >= len(x.children):
                return
            rsnode = x.children[j]
            if i < len(x.address):
                cnode.address.append(x.address[i])
                for k in range(len(rsnode.address)):
                    if rsnode.address[k] is not None:
                        cnode.address.append(rsnode.address[k])
                        if len(rsnode.children) > k:
                            cnode.children.append(rsnode.children[k])
                if len(rsnode.children) > len(rsnode.address):
                    cnode.children.append(rsnode.children[-1])
                new = cnode
                x.address.pop(i)
                x.children.pop(j)
        else:
            lsnode = x.children[j]
            if j < len(x.address):
                lsnode.address.append(x.address[j])
                for k in range(len(cnode.address)):
                    if cnode.address[k] is not None:
                        lsnode.address.append(cnode.address[k])
                        if len(cnode.children) > k:
                            lsnode.children.append(cnode.children[k])
                if len(cnode.children) > len(cnode.address):
                    lsnode.children.append(cnode.children[-1])
                new = lsnode
                x.address.pop(j)
                x.children.pop(i)

        if x == self.root and len(x.address) == 0:
            self.root = new

    def delete_sibling(self, x, i, j):
        cnode = x.children[i]
        if i < j:
            rsnode = x.children[j]
            cnode.address.append(x.address[i])
            x.address[i] = rsnode.address[0]
            if len(rsnode.children) > 0:
                cnode.children.append(rsnode.children[0])
                rsnode.children.pop(0)
            rsnode.address.pop(0)
        else:
            lsnode = x.children[j]
            cnode.address.insert(0, x.address[i - 1])
            x.address[i - 1] = lsnode.address.pop()
            if len(lsnode.children) > 0:
                cnode.children.insert(0, lsnode.children.pop())

def load_imagem(pasta):
    formatos = (".png", ".jpeg", ".jpg")

    arquivos = ([os.path.join(pasta, f) for f in os.listdir(pasta) if f.lower().endswith(formatos)])

    arquivos = sorted(arquivos, key=lambda x: int(re.search(r'\d+', os.path.basename(x)).group()))

    imagens = sorted([(os.path.basename(arq), Image.open(arq)) for arq in arquivos])

    return imagens

def main():
    B = B_Tree(3)

    inicio = time.time()

    for i in range(50_000):
        B.insert(f"{i}")

    inicio = time.time()  

    B.print_inOrder(B.root)

    fim = time.time()

    print(f"Tempo de execução: {fim - inicio}")


main()