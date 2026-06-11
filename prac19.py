"""Calculate income tax for a given income based on these rules:
First $10,000: 0% tax
Next $10,000: 10% tax
Remaining income: 20% tax"""

def calculate(income):
    if income <= 10000:
        return 0
    elif income <= 20000:
        return (income -10000) * 0.1
    else:
        return (income -20000)* 0.2 + 10000 * 0.1


calculated_tax = calculate(45000)
print(calculated_tax)