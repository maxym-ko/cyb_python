import math


def info_author():
    about_author = f"\
    Author: Koval\n\
            Maxym\n\
    Group: К-12\n"
    print(about_author)


def is_number(s: str) -> bool:
    """Check if s can be represented as a number"""
    try:
        float(s)
        return True
    except ValueError:
        return False


def domain(x: float) -> float:
    """Check if x is in domain of an expression"""
    return x - 5 and x + 6 and x + 12


def f(x: float) -> float: # Чи треба писати, який вираз вираховується?
    """Calculate the next expression: cos(29/63) - 22e/51pi * 10 / ((x - 5)(x - 6)) + 7sin(x - 8) - 5 / (x + 12)"""
    return math.cos(29 / 63) - 22 * math.e / 51 / math.pi * 10 / (x - 5) / (x + 6) + 7 * math.sin(x - 8) - 5 / (x + 12)


def f_total(x: float) -> bool and float:
    """
    Calculate expression if it is possible
    Return True if calculation is successful or False if not and result of calculation
    """
    if domain(x):
        return True, f(x)
    else:
        return False, -1


def run():
    print('Variant 71 \nThis program calculate an expression using variables, entered by the user')
    info_author()

    x = input('Input a value of x: ')

    if not is_number(x): # Якшо тут повернути -1, і продовжувати програму не в else?
        print('\nwrong input \nYou have input a value of x that can\'t be represented as a number. Please, restart program and try again.')
    else:
        print('\n***** do calculations ... ', end='')
        x = float(x)
        success, result = f_total(x)
        print('done\n')

        print(f'for x = {x:.6f}')
        if success:
            print(f'result = {result:.6f}')
        else:
            print(f'result = undefined \n(result can\'t be calculated because x = {x} isn\'t in domain of a function.)')


run()
