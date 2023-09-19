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


BANNED_WORDS = ['прыщ', 'редиска', 'кошак', 'шторм']


@register.filter(name='censor')
def censor(value):
    for word in BANNED_WORDS:
        value = value.replace(word, '*' * len(word))
    return value
