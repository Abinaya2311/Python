def capfirst(word):
    if word.isalpha():
        s = word[0].upper() + '.'
        return s
    else:
        return ""  
sentence=input("Enter a sentence: ")
list=sentence.split()
req=""
for word in list:
    req=req+capfirst(word)
print(req)
