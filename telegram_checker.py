import subprocess
import time
import telegram

bot = telegram.Bot(token="PUT TELEGRAM TOKEN HERE")
chat_id=PUT CHAT ID HERE

if __name__ == '__main__':
    while True:
        time.sleep(5)
        p = subprocess.Popen("sudo arp-scan -l | grep PUT MAC ADDRESS HERE", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        if output:
            bot.sendMessage(chat_id=chat_id, text="Johnny is home!")
            exit
        else:
          time.sleep(1)
