# telegram-wifi-checker
Check if someone connects to Wifi and send a telegram message as trigger

Install requirements:

sudo apt install python-pip && sudo apt install arp-scan && sudo pip3 install python-telegram-bot

Then check the MAC adress of the device you want to keep checking with:

sudo arp-scan -l

Then download the python file, put it in /home/pi and change MAC adresss with the MAC adress you just found.
Afterwards, download the telegram app, open a chat with @BotFather and type /newbot
Now, send a message, check chat id, and fill in token and chat-id into the python file.

When all is complete, you can run:

python3 telegram_checker.py

Now, you will get a message when the person's phone or tablet connects to the wifi network. You will need to run it again to track further connects. 
