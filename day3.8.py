class Solve():
   def Anagrams( self, li ):
       '''
       Function to Group Anagrams
       :param li: list of words
       :return: list of grouped anagrams
       '''
       dictionary = {}
       for word in li:
           sortedWord = ''.join(sorted(word))
           if sortedWord not in dictionary:
               dictionary[sortedWord] = [word]
           else:
               dictionary[sortedWord] += [word]
       return [dictionary[i] for i in dictionary]
if __name__ == '__main__':
   li = "12345"
   print(Solve().Anagrams(li))
