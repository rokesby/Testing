from vowel_remover import VowelRemover

remover = VowelRemover("aeiou")
result_no_vowels = remover.remove_vowels()
print("Result : ", result_no_vowels)