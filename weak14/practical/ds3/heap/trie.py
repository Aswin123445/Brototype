class Node:
    def __init__(self):
        self.child = {}
        self.end_of_word = False 
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self,word):
        current = self.root 
        for c in word :
            if c not in current.child:
                current.child[c] = Node()
            current = current.child[c]
        current.end_of_word = True 
        
    def search(self,word):
        current = self.root 
        for c in word :
            if c not in current.child:
                return False 
            current = current.child[c]
        return current.end_of_word
        
    def has_prefix(self,word):
        current = self.root 
        for c in word :
            if c not in current.child:
                return False 
            current = current.child[c]
        return True 
        
    def delete(self,word):
        self._delete(self.root,word,0)
        
    def _delete(self,current,word,index):
        if len(word) == index :
            if not current.end_of_word :
                return False 
            current.end_of_word = False 
            return len(current.child) == 0 
        c = word[index]
        next_node = current.child.get(c)
        if next_node is None :
            return False 
        delete_node = self._delete(next_node,word,index+1)
        if delete_node:
            del current.child[c]
            return len(current.child) == 0 and not current.end_of_word    
        return False 
        
    def start_with(self,prefix):
        current = self.root
        word = []
        for c in prefix :
            if c not in current.child :
                return word 
            current = current.child[c]

        def _dfs(current,path):
            if current.end_of_word:
                word.append(''.join(path))
            for c,node in current.child.items():
                _dfs(node,path+[c])
        _dfs(current,list(prefix))
        return word
        
    def auto_complete(self, prefix):
        current = self.root
        for c in prefix:
            if c not in current.child:
                return None  # No matching word found
            current = current.child[c]
        
        # Perform DFS to find the first complete word
        def _dfs_first(current, path):
            if current.end_of_word:
                return ''.join(path)
            for c, node in current.child.items():
                result = _dfs_first(node, path + [c])
                if result:
                    return result
            return None
    
        return _dfs_first(current, list(prefix))

# Add this method to your Trie class

        
trie = Trie()
words = ["app", "apple", "apex", "apply", "application", "applet"]
for word in words:
    trie.insert(word)

# Testing autocomplete
print(trie.start_with("ape"))  # Output: ['app', 'apple', 'apply']
print(trie.start_with("bat"))  # []
print(trie.start_with("a"))    # ['apple', 'apply']