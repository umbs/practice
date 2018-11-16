
class Node:
    def __init__(self):
        self.is_word = False
        self.edge = {}  # empty dictionary


class Trie:
    '''
    insert, find, delete, prefix_match
    '''
    def __init__(self):
        self.root = Node()


    def insert(self, root, word):
        for c in word:
            if c in root.edge:
                root = root.edge[c]
            else:
                root.edge[c] = Node()
        root.is_word = True


    def find(self, root, word):
        for c in word:
            if c in root.edge:
                root = root.edge[c]
            else:
                return False

        return root.is_word


    def delete(self, root, word):
        '''
        rewinding the stack??
        '''
        pass


    def prefix_match(self, root, word):
        for c in word:
            if c in root.edge:
                root = root.edge[c]
            else:
                return False

        return True
