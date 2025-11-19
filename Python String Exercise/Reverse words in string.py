def reverse_words(string):
    res= ' '.join(string.split()[::-1])
    return res
    

strg= 'My name is Ankita'
res= reverse_words(strg)
print(res)