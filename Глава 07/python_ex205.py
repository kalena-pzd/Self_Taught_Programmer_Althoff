qs = ["Как тебя зовут?",
      "Твой любимый цвет?",
      "Что ты делаешь?"]
n = 0
while True:
    print("Введи Х для выхода")
    a = input(qs[n])
    if a == "Х":
        break
    n = (n + 1) % 3
