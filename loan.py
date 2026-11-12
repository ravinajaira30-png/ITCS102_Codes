loan_amount = float(input("Enter the loan amount: "))
years = int(input("enter the number of years:"))
months = years * 12
principal = loan_amount / months
#remaining_balance = loan_amount
#loan_interest = pass
#monthly_pay = pass

print("Month\t\tMonthly Payment\t\tPrincipal\t\tInterest\t\tRemaining Balance")
for x in range (1, months + 1):
    remaining_balance = loan_amount - (principal * x)
    loan_interest = remaining_balance * 0.00256
    monthly_pay = principal + loan_interest
    

    print(f"| {x}\t\t{round(monthly_pay,2)}\t\t|\t{round(principal,2)}\t\t|\t{round(loan_interest,2)}\t\t|\t{round(remaining_balance,2)}\t\t|")
