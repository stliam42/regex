import re

text = '''Было закуплено 12 единиц техники
по 410.37 рублей.

0.32
0.003
3,1
334.344.344'''

regex = r'\d+(?:(?:,|.)\d+)?'

#result = re.findall(regex, text)

#for number in result:
#    print(number.replace(',', '.'))

text = re.sub(r'\d+,\d+', lambda x: x.group().replace(',', '.'), text)
result = re.sub(regex, lambda x: str(float(x.group())**3), text)

print(result)
