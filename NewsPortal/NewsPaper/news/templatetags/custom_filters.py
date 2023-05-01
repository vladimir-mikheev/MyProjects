from django import template


register = template.Library()


CURRENCIES_SYMBOLS = {
   'rub': 'Р',
   'usd': '$',
}


@register.filter()
def currency(value, code='rub'):
   """
   value: значение, к которому нужно применить фильтр
   code: код валюты
   """
   postfix = CURRENCIES_SYMBOLS[code]

   return f'{value} {postfix}'


BANNED_WORDS = ['bad', 'words', 'to', 'censor']

@register.filter(name='censor')
def censor(value):
    """
    A filter that censors the banned words in a string
    """
    for word in BANNED_WORDS:
        value = value.replace(word, '*' * len(word))
    return value
