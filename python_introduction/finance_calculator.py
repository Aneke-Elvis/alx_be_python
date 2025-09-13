# finance_calculator
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses
print(monthly_savings)

#Calculate projected annual savings
interest_rate = 0.05 
one_yearly = 12
projected_savings = monthly_savings * one_yearly + (monthly_savings * one_yearly * interest_rate)
print(f"Projected savings after one year, with interest, is: {projected_savings}")