vowels = ['a','e','i','o','u']
h = raw_input("Give me a sentence").lower()
for x in vowels:#it looks for each letter in the sentence is in vowels
    h = h.replace(x,'')#it replace all the letter that are vowel it replace them with nothing 
print h
