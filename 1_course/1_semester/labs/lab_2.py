from math import fabs

a, b = -0.9, 0.9


def s(x: float, eps: float = 10e-6) -> float:
    """Calculate the value of the function for x with accuracy eps"""
    k = 5
    a_k = x
    sum = a_k
    x_4 = x**4
    while fabs(a_k) >= eps:
        a_k *= x_4 * (k - 4) / k
        sum += a_k
        k += 4
    return sum


def domain(x: float) -> bool:
    """Check if x is in the domain of the function"""
    return a <= x <= b


def s_total(x: float, eps: float = 10e-6) -> float:
    """
    Calculate the value of the function for x with accuracy eps if it is possible
    Return True if calculation is successful or False if not and the result of the calculation
    """
    if not domain(x) or eps < 0:
        return False, None
    else:
        return True, s(x, eps)


def info_author():
    about_author = f"\
    Author: Koval\n\
            Maxym\n\
    Group:  К-12\n"
    print(about_author)


def main():
    print("Variant #71 \nThis program calculate the value of a function using argument and accuracy, entered by the "
          "user")
    info_author()

    x = input("Input an argument value: ")
    eps = input("Input the accuracy of the calculation: ")

    try:
        x = float(x)
        eps = float(eps)
    except ValueError:
        print("\n***** Error\nYou have input an argument value or an accuracy value that can't be "
              "represented as a number. Please, restart program and try again.")
    else:
        print("\n***** do calculations ... ", end="")
        success, result = s_total(x, eps)
        print('done\n')

        print(f"for x = {x:.6f}")
        print(f"for eps = {eps:.4E}")
        if success:
            print(f"result = {result:.8f}")
        else:
            print(f"result = undefined \nThe result can't be calculated because x = {x} isn't in domain of a function.")


main()
