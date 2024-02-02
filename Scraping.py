from bs4 import BeautifulSoup                     #Abenezer-Girum
import requests
import sys
import io
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


bot_token = '6746701496:AAG4codyBDE-9W7jyUGM43X2ou3vh1Burl0'
chat_id = ''# please enter you own chat_id and try it and start a conversation with the bot before doing this

response = requests.get('https://www.ethiopianreporter.com/')
soup = BeautifulSoup(response.text, 'lxml')
news_entries = soup.find_all('h3', class_='entry-title td-module-title')


def send_to_telegram(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, params=params)
    return response.json()

for entry in news_entries:
    alink = entry.find('a', href=True)

    if alink:
        title = alink.get_text(strip=True)
        link = alink['href']
        message = f"News: {title}\nLink: {link}\n"
        response = send_to_telegram(bot_token, chat_id, message)
        time.sleep(15)

