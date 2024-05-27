# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagrams = []
        for w in words:
            # Convert both the current word and the target word to lowercase
            lowercase_w = w.lower()
            lowercase_self_word = self.word.lower()
            
            # Check if the current word is not identical to the target word, but they are anagrams
            if lowercase_w != lowercase_self_word and sorted(lowercase_w) == sorted(lowercase_self_word):
                # If they are anagrams, append the current word to the list of anagrams
                anagrams.append(w)
        
        # Return the list of anagrams
        return anagrams
    pass