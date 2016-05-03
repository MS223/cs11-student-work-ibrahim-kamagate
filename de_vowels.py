vowels = ['a','e','i','o','u']
h = raw_input("Give me a sentence").lower()
for x in vowels:
    h = h.replace(x,'')
print h
