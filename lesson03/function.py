# original

name1 = 'Марина'
h1 = 1.70
w1 = 61

name2 = 'Лена'
h2 = 1.70
w2 = 75


def bmi_calculator(name, h, w):
    bmi = w/(h**2)
    print(name + ": Индекс массы тела = " + str(bmi))
    if bmi<=25:
        return name + " может скушать пончик"
    else:
        return name + " пора садиться на диету"

bmi1 = bmi_calculator(name1, h1, w1)
bmi2 = bmi_calculator(name2, h2, w2)

print(bmi1)
print(bmi2)

# fixed


def show_person_bmi(name, weight, height):
    bmi = calculate_bmi(weight, height)
    print("%s: Индекс массы тела = %.2f" % (name, bmi))


def show_person_weight_advice(name, weight, height):
    bmi = calculate_bmi(weight, height)
    advice = get_advice_on_bmi(bmi)
    print(f"{name} {advice}")


def calculate_bmi(weight, height):
    return weight / height**2


def get_advice_on_bmi(bmi):
    if bmi <= 25:
        return "может скушать пончик"
    else:
        return "пора садиться на диету"


print("FIXED")

show_person_bmi(name1, w1, h1)
show_person_bmi(name2, w2, h2)

show_person_weight_advice(name1, w1, h1)
show_person_weight_advice(name2, w2, h2)
