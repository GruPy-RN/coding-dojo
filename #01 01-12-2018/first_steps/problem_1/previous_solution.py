from math import sqrt

def solve_bhaskara(a, b, c):
    if a == 0:
        return "Impossivel calcular"

    delta = b**2 - 4*a*c
    if delta < 0:
        return "Impossivel calcular"
    x1 = (-b + sqrt(delta)) / (2*a)
    x2 = (-b - sqrt(delta)) / (2*a)

    return ("Raiz 1: {:.5f}".format(x1), "Raiz 2: {:.5f}".format(x2))