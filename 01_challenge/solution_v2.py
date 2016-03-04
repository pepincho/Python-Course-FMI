BMI_PRECISSION = 1

CATEGORIES = {
    'тежко недохранване': (float('-inf'), 15),
    'средно недохранване': (15, 16),
    'леко недохранване': (16, 18.5),
    'нормално тегло': (18.5, 25),
    'наднормено тегло': (25, 30),
    'затлъстяване I степен': (30, 35),
    'затлъстяване II степен': (35, 40),
    'затлъстяване III степен': (40, float('inf')),
}

def body_mass_index(weight, height):
    return round(weight / height ** 2, BMI_PRECISSION)


def shape_of(weight, height):
    BMI = body_mass_index(weight, height)
    for category, interval in CATEGORIES.items():
        if interval[0] < BMI <= interval[1]:
            return category
