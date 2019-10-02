#!/usr/bin/python3
# Python v3.6+ required
import requests
import time
import pprint


discord_token = 'YOUR_DISCORD_TOKEN'
pubkey =        'YOUR_PUBLIC_KEY'

faucet_timeout = (60 * 60 * 3) + 5    # 10805 sec --> 3 hours
faucet_url =    'https://discordapp.com/api/v6/channels/603658949182488580/messages'
post =          '{"content":"$request $addr$","tts":false}'.replace('$addr$', pubkey)
headers =       {"Authorization": discord_token, "Content-Type": "application/json"}


def send_message(p, h):
    try:
        print(f'Trying to send message:\n{p}')
        req = requests.post(url=faucet_url, data=str(p), headers=h)
        data = req.content
        if req.status_code == 200:
            print('success', req.status_code)
            # pprint.pprint(data)
            return data
        else:
            print('ERROR:', req.status_code)
            pprint.pprint(data)
            return 'err'

    except (requests.RequestException, Exception) as connectErr:
        print(connectErr)
        return 'err'


while True:
    result = send_message(post, headers)
    # retry if fail
    while result == 'err':
        # wait 5 minutes
        time.sleep(300)
        result = send_message(post, headers)
    print(f'Waiting {faucet_timeout / 3600} hours')
    time.sleep(faucet_timeout)
