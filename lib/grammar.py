# File: lib/challenge_grammar.py

class GrammarStats:
    def __init__(self):
        self.checks = []

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise


        # Check the first and last character of the string.
        if (text[0].isupper()) and (text[-1] == "."):
            self.checks.append(True)
            return True
        else:
            self.checks.append(False)
            return False
        
        # Store the result


    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass
