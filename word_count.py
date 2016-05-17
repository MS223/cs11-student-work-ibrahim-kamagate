text_input = raw_input("Paste your text here").lower()
text_input = text_input.replace("."," ")
text_input = text_input.split()
words = raw_input("What words do you want to look for?").lower()
words = words.replace(","," ")
words = words.split()
text = {

}
text['word count'] = text_input.count(words)
for x in text_input:
    if x in words:
        text[x]=text_input.count(x)
print text[words]

