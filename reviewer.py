age = int(input("enter your age: "))
monthly_revenue = float(input("monthly revemue: "))
cc = int(input("credit score: "))
has_defaults = bool(input("file for bankcruptcy: "))
collaterals = input("collaterals: ")
c_value = float(input("collateral value: "))

maximum_loan = 0
base_fee = 0
if age >=21 and has_defaults == False and years >= 2.0: #teir 1
    print("baseline passed")
    if cc >= 720:
        print("credit score is high ")
        maximum_loan = 3 * monthly_revenue 
        if monthly_revenue >= 50000:
            maximum_loan = * monthly_revenue 0.015
            print("base fee is set to",base_fee)
        else:
            print("revenue below 50k")
            base_fee = maximum_loan * 0.025
            print("base fee is set to",base_fee)

    elif cc <= 620 and credit_score <=720: #teir 2
        print("credit score too low")
        maximum_loan = monthly_revenue * 1.5
    else:
        print("invalid")

    elif cc <620: #teir 3
        print("credit is too low")
    


else:
    print("baseline failed")

