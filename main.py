import json
from dhooks import Webhook
import requests
import time
hook = Webhook('WEBHOOK HERE')
url = 'https://api.coingecko.com/api/v3/simple/price?ids=Monero&vs_currencies=usd'
while True:
    try:
        r = requests.get(url)
        price = json.dumps(r.json()['monero']['usd'])
        print(price)
        hook.send(price)
        time.sleep(3600)
    except Exception as e:
        print(e)