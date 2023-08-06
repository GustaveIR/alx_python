from decimal import Decimal, getcontext

def pow(a, b):
    getcontext().prec = 21
    a_decimal = Decimal(a)
    b_decimal = Decimal(b)
    result = a_decimal ** b_decimal
    return float(result)
