# Inputs
principal = float(input("Please enter the initial loan amount: "))
annual_rate = float(input("Please thent the annual interest rate (e.g., 5.5): ")) / 100
monthly_payment = float(input("Please enter monthly payment amount: "))

# Constants for calculation
DAYS_IN_YEAR = 365
DAYS_IN_MONTH = 30.42 # (Standard number used in these daily balance method interest calculations)
daily_rate = annual_rate / DAYS_IN_YEAR # Rate of daily interest accrual for daily balance method

balance = principal
payment_number = 0

# Print the header
print("\nPmt # | Balance      | Interest  | Principal")
print("-" * 45)

#The calculation loop
while balance > 0:
    payment_number += 1
    # calculate interest for this period 
    interest_payment = balance * daily_rate *DAYS_IN_MONTH
    # Calculate how much goes to the principal
    principal_payment = monthly_payment - interest_payment
    # Check if this is the final payment
    if balance < principal_payment:
        principal_payment = balance
        balance = 0
    else:
        balance = balance - principal_payment
    #output the results for this month
    print(f"{payment_number:<5} | ${balance:<10.2f} | ${interest_payment:<8.2f} | ${principal_payment:<8.2f}")

print("-" * 45)
print("Loan paid off!")