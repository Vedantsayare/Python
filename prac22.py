#Write a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.

def exponent(base,exp):
    result = 1

    for _ in range(exp):
        result *= base
    return result

print(exponent(2,7))