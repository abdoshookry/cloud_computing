import re

f = open('Pride and Prejudice.txt','r', encoding = 'utf-8')
f2 = open('Beyond the Wall of Sleep.txt','r', encoding = 'utf-8')

text = f.read()
text2 = f2.read()

f.close()
f2.close()

words = re.split("[\W]+|[_]",text.lower())
words2 =  re.split("[\W]+|[_]",text2.lower())

def rm(words):
    for i,word in enumerate(words):
        if(words[i] == "chapter"):
            del words[i]
            del words[i]

rm(words)
rm(words2)

unique = set(words)
unique2 = set(words2)
common = unique.intersection(unique2)
common.remove("")
print(common)
