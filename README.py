from random import choice
def coin_flip():
    eagle = 0
    tails = 0
    options = ["eagle", "tails"]
    total = int(input("Введите количество подбрасываний: "))
    throw = total
    while throw >= 1:
        if choice(options) == "eagle":
            eagle += 1
        else:
            tails += 1
        throw -= 1
    percent = float((eagle / total) * 100)
    percent_ideal = abs(50 - percent)
    return eagle, tails, percent, percent_ideal
while True:
    eagle, tails, percent, percent_ideal = coin_flip()
    print(f"Орлов: {eagle}")
    print(f"Решек: {tails}")
    print(f"Процент орлов: {percent}%")
    print(f"Отклонение от идеала: {percent_ideal}%")
