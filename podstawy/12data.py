import datetime

print(str(datetime.datetime.now().hour) + ":" + datetime.datetime.now().strftime("%M"))

teraz = datetime.datetime.now()
print(teraz.strftime("%I:%M %p %d.%m.%Y %b %B"))