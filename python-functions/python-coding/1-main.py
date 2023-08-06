#!/usr/bin/env python3
pow = __import__('python-functions.1-power').pow

result = pow(-98, -10)
formatted_result = "{:.20f}".format(result)
print(formatted_result)
