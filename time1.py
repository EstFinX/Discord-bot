from datetime import datetime

def get_time():
    t = datetime.now()
    print("Текущее время: {}:{}:{}.".format(t.hour+3, t.minute, t.second))
