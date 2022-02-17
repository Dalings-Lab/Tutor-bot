def bilet(numero):
    numros_of_bilets = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20]
    my_bilet = list()

    if numero == 1:
        numero = 0
    elif numero in numros_of_bilets:
        numero = numero * 4 - 4
    else:
        return "Данного билета не существует"

    with open('questons.txt') as file:
        lines = file.readlines()
        for i in range(4):
            my_bilet.append(lines[numero])
            numero += 1
    return my_bilet


def text_of_bilet(numero):
    all_spisok = ''
    for z in bilet(numero):
        all_spisok += z
    return all_spisok



