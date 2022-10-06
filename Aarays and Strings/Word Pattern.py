# // Code to find a word pattern 

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Understood the usage of Hashmap and the positional plcement of key and values inorder to fing the unordered pair
# a --> dog b --> cat and viceversa 

def wordPattern(pattern: str, s: str) -> bool:
    charword = {}
    wordchar = {}
    word = s.split(" ")
    if len(pattern) != len(word):
            return False
    for c,w in zip(pattern,word):
            if c in charword and charword[c] != w:
                return False
            if w in wordchar and wordchar[w] != c:
                return False
            charword[c] = w
            wordchar[w] = c
    return True
print(wordPattern("abba","dog cat cat dog"))