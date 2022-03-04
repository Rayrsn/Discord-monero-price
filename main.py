import requests
import time
from datetime import datetime
from dhooks import Webhook
from datetime import datetime
from kavenegar import KavenegarAPI


#CONFIG
IDS = 'monero'
CURRENCY = 'usd'

# OPTIONAL

# if send by discord web hook
WEBHOOK = ''


# get it from kavenegar.com
# if send by sms
PHONE_NUMBER = ''


def get_price():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={IDS}&vs_currencies={CURRENCY}"
    r = requests.get(url)

    price = r.json()[IDS][CURRENCY]
    time = datetime.now()
    return f"{IDS}   is    {price}     {CURRENCY}'s    ---         {time}" 


def send_by_sms(kavenegar_api_key):
    api = KavenegarAPI(kavenegar_api_key)
    price = get_price()
    payload = {
        "sender": '8585858585858585',
        "receptor" : PHONE_NUMBER,
        'message': price,
    }
    res = api.sms_send(params=payload)
    print (res)

def send_to_discord():
    hook = Webhook(WEBHOOK)
    price = get_price()
    hook.send(price)

while True:
    try:
        send_by_sms()
        time.sleep(3600)
    except Exception as e:
        print(e)
