# Calculating income tax

def cal_income_tax(income,deduction):
    tax = income - deduction

    tax = 0

    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - deduction) * 0.05
    elif income <= 1000000:
        tax = (income - deduction) * 0.05 + (income - deduction) * 0.20
    else:
        tax = (income - deduction) * 0.05 + (income - deduction) * 0.20 + (income - deduction) * 0.30
    
    return tax


income = float(input("Enter your income : "))
deduction = float(input("Enter deduction : "))

total_tax = cal_income_tax(income,deduction)
print("Total income tax : ",total_tax)