import asyncio
import json
from django.http import HttpResponse
from .bot import bot, bot_tele  # Импортируем bot из bot.py

def index(request):
    if request.method == 'POST':
        data = request.body
        res = json.loads(data.decode('utf-8'))
        print(res)  # Выводим полученные данные в консоль для отладки
        asyncio.run(bot_tele(res))
        return HttpResponse("ok")
    else:
        return HttpResponse("hello world!")
