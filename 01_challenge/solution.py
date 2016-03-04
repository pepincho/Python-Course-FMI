BMI_PRECISSION = 1


def body_mass_index(weight, height):
    return round(weight / height ** 2, BMI_PRECISSION)


def shape_of(weight, height):
    BMI = body_mass_index(weight, height)
    if BMI <= 15:
        return 'тежко недохранване'
    elif BMI > 15 and BMI <= 16:
        return 'средно недохранване'
    elif BMI > 16 and BMI <= 18.5:
        return 'леко недохранване'
    elif BMI > 18.5 and BMI <= 25:
        return 'нормално тегло'
    elif BMI > 25 and BMI <= 30:
        return 'наднормено тегло'
    elif BMI > 30 and BMI <= 35:
        return 'затлъстяване I степен'
    elif BMI > 35 and BMI <= 40:
        return 'затлъстяване II степен'
    else:
        return 'затлъстяване III степен'
