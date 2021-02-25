# original

def bmi_calculator(name, h, w):
    bmi = w/(h**2)
    print(name + ": Индекс массы тела = " + str(bmi))
    if bmi<=25:
        return name + " может скушать пончик"
    else:
        return name + " пора садиться на диету"

# fixed
