import re

text = "Он --- серо-буро-красно-серо-малиновая редиска!!  >>>:->  А не кот.  www.kot.ru"

regex = r'\w+[-*\w*]*'

words = re.findall(regex, text, flags=re.IGNORECASE)

print(words)
