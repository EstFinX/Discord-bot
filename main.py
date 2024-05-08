print("Привет!")
Запрос1=input("Введите запрос:").lower()
if "время" in Запрос1 or "времени" in Запрос1:
    from smartbot import time1
    time1.get_time()
elif "переведи" in Запрос1 or "перевести" in Запрос1:
    from smartbot import translator
    Текст=input("Введите текст для перевода:")
    translator.translate(Текст)
elif "погода" in Запрос1 or "температура" in Запрос1:
    from smartbot import weather
    #Текст=input("Введите текст для перевода:")
    weather.get_weather(Запрос1)
elif "вычисли" in Запрос1 or "умножь" in Запрос1 or "сколько будет" in Запрос1:
    from smartbot import calculator
    #Текст=input("Введите текст для перевода:")
    calculator.calculate(Запрос1)
else:
    from smartbot import ChatGPD
    ChatGPD.ChatGPD1(Запрос1)
