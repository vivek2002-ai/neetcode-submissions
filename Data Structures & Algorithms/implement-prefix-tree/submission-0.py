class TrieNode:
    def __init__(self, letter:str):
        self.value = letter
        self.children = []
        self.is_last_letter = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode('*')
        
    def insert(self, word: str) -> None:
        curNode = self.root
        for letter in word:
            is_letter_present = False
            for child in curNode.children:
                if child.value == letter:
                    is_letter_present = True
                    curNode = child
                    break
            if is_letter_present==False:
                newNode = TrieNode(letter)
                curNode.children.append(newNode)
                curNode = newNode
        curNode.is_last_letter = True
        return None

    def search(self, word: str) -> bool:
        curNode = self.root
        for letter in word:
            is_letter_present = False
            for child in curNode.children:
                if child.value == letter:
                    is_letter_present = True
                    curNode = child
                    break
            if is_letter_present == False:
                return False
        return curNode.is_last_letter

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for letter in prefix:
            is_letter_present = False
            for child in curNode.children:
                if child.value == letter:
                    is_letter_present = True
                    curNode = child
                    break
            if is_letter_present==False:
                return False
        return True
        
        