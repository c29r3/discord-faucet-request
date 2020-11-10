# discord-faucet-request
Auto request tokens via Discord faucet every 3 hours

# DISCLAIMER  
Discord started getting banned for automating account management. I don't recommend using this method anymore.

# Requirements
Python v. 3.6+

# How to start
1. Clone repo - `git clone https://github.com/c29r3/discord-faucet-request.git && cd discord-faucet-request`
1. Go to your discord client (desktop\web) 
2. Press `ctrl + shift + i`
3. Go to tab `Network`
4. Press `F5`
5. Write in the search field `mes` and choose `messages?limit=50`
6. In the `Headers` tab, find the `authorization` parameter and copy key value to the variable `discord_token` in `faucet_request.py`\
![alt text](http://i.imgur.com/zp2BlOY.png "example")
7. Copy your coda public key to variable `pubkey` in `faucet_request.py`
8. `chmod u+x faucet_request.py`
9. Start the script `python3 faucet_request.py`

# Note
Just keep in mind that this authorization token gives full access to the Discord account. It must not be shown to anyone

You can create a binary file for this script, then no one can see the specified token. 
On Ubuntu machine:\
`sudo apt install python3-pip`\
`pip3 install pyinstaller`\
`pyinstaller -F faucet_request.py`

If everything is ok, then you will get an executable file in the folder dist. Other created folders can be deleted.
