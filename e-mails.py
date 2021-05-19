import re

text = """
Иван Иванович! 
Нужен ответ на письмо от ivanoff@ivan-chai.ru. 
Не забудьте поставить в копию 
serge'o-lupin@mail.ru- это важно.
"""

regex = r"\w[\w'._+-]{1,63}\w@[a-z0-9][a-z0-9.-]{0,253}[a-z0-9]"
emails = re.findall(regex, text, flags=re.IGNORECASE)

print(emails)
