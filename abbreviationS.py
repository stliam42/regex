import re

text = '''Это курс информатики соответствует ФГОС и ПООП, 
это подтверждено ФГУ ФНЦ НИИСИ РАН'''
regex = r'[А-Я]{2,}(?:\s[А-Я]+)*'

result = re.search(regex, text)

print(result.start())
