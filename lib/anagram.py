# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word= word
        self.sorted_word= self.sort_word(word)
    def sort_word(self, word):
        return ''.join(sorted(word))

        
       
    def match(self, possible_anagrams):
        match= []
        for candidate in possible_anagrams:
           if self.sort_word(candidate)== self.sorted_word:
               match.append(candidate)
        return match  
    
    
anagram = Anagram('listen')
print(anagram.match(['enlists','google','inlets', 'banana']))
    
        