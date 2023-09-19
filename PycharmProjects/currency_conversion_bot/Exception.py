import requests
import json
from config import keys

class APIException(Exception):
    pass

class CurrencyConvertor:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        quote = quote.lower()
        base = base.lower()
        if quote == base:
            raise APIException("Невозможно конвертировать одинаковые валюты")
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту <{base}>, проверьте правильность написания')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту: <{quote}>, проверьте правильность написания')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать валюту в количестве: {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        total_base = total_base * amount

        return total_base