import requests
import json
from config import exchanges

class ApiException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        try:
            base_key = exchanges[base]
        except KeyError:
            raise ApiException(f'Valuutat {base} ei leitud!')
        try:
            quote_key = exchanges[quote]
        except KeyError:
            raise ApiException(f'Valuutat {quote} ei leitud!')

        if base_key == quote_key:
            raise ApiException(f'Ei saa osta sama valuutat {base}!')

        try:
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise ApiException(f'Ei suutnud valuutakogus töödelda  {amount}!')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_key}&tsyms={quote_key}')
        new_price = json.loads(r.content)[exchanges[quote]] * amount

        return round(new_price, 2)
