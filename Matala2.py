# -*- coding: utf-8 -*-
#A    
def reverse(sentence,reverse_word):
    word = sentence.split()
    for i in word:
        if  i == reverse_word:
            reverse=reverse_word[::-1]
            x = sentence.replace(reverse_word, reverse,1)
            return(x)
            
        
    if type(reverse_word)!= str:
        return("invalid input detected")
            
        
    else:
        return("no match word found")
        

print(reverse('I like apples and I also like bananas','like'))

#%%




