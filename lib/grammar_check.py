class GrammarStats:
    def __init__(self):
        self.check_list = []

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise


        # Check the first and last character of the string.
        if (text[0].isupper()) and (text[-1] == "."):
            self.check_list.append(True)
            return True
        else:
            self.check_list.append(False)
            return False
        
        # Store the result


    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        running_total = 0
        #print(self.check_list)
        for item in self.check_list:
            if item:
                # Then the line contained good grammar.
                running_total +=1
        if running_total == 0:
            return 0
        else:
            return running_total/len(self.check_list)*100        


