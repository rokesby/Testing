# File: lib/vowel_remover.py

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            else:
                i += 1
        return self.text

# As the counter increases, i will be 3 and higher then the length of 'eo' and loop terminates prematurely.
# Also the loop counter is skipping 'e' and moving straight to 'i'

#remover = VowelRemover("aeiou")
#print("Result : ", remover.remove_vowels())
