#Here we're going to call the functions we created and print the result

from functions import *
import operator #I didn't like how the output looked, so I found a metod to make it look a bit better

text = "Hi, this is going to be an example of a particular case. Is it gonna be difficult? I don't think so, but maybe it can be!"

lowerCase = toLowerCase(text) 

cleanedText = cleanText(lowerCase)

splittedText = splitText(cleanedText)

numWords = countedWords(splittedText)

numWordsSorted = sorted(numWords.items(), key=operator.itemgetter(1),reverse=True) #This is the line that makes the output look a little bit better

print(numWordsSorted)

#I think I could've written this in a more efficient way (e.g. I think I could've put the function splitText inside the function cleanText)
#I'm still learning, so I'll be glad if I receive suggestions