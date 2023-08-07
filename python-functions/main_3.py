#!/usr/bin/python3
from decimal import Decimal, getcontext
from python-functions.1-power import power

# Set the precision to 20 decimal places
getcontext().prec = 20

result = power(-98, -10)
formatted_result = format(Decimal(result), '.18e')
print(formatted_result)
