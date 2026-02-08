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