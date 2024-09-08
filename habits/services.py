import requests
from django.conf import settings


def tg_send(habit):
    text = f"Пора делать {habit.action}!"
    chat_id = habit.user.tg_chat_id
    params = {"text": text, "chat_id": chat_id}

    response = requests.get(
        f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage",
        data=params
    )
    if response.status_code != 200:
        print(f"Error sending message to Telegram: {response.status_code}")
