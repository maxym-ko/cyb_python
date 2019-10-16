def is_collinear_lines(a1: float, b1: float, a2: float, b2: float) -> bool:
    # pre: a2 != 0 and b2 != 0
    if a1 / a2 == b1 / b2:
        return True
    return False
