from email.mime import base


age = int(input("Enter your age: "))
is_employed = bool(input("Are you employed? (yes/no): "))
credit_score = float(input("Enter your credit score: "))
anual_income = float(input("Enter your annual income: "))
has_collateral = bool(input("Do you have collateral? (true/false): "))

interest_rate = 0.0

if age >= 21 and is_employed == true:
    print("accepted")
    if credit_score >= 750:
        print("you have a good credit score")
    if annual_income >= 100000:
        base_rate = 4.5 
        print("your base rate is: ", base_rate)
    else:
        base_rate = 5.0
        print("base



