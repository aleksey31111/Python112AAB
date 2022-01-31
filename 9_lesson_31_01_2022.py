import time
import locale

locale.setlocale(locale.LC_ALL, "ru") # ""

print("Продолжение Урока 8 ( 15, 16 )")

# start = time.time()
start = time.monotonic() # Более точное время
time.sleep(0.1)
finish = time.time()
result = finish - start
print(result)

print((time.strftime("Сегодня: %B %d, %Y", time.localtime())))
print((time.strftime("Сегодня: %B %d, %Y", time.localtime())))

print("Скачать Git")