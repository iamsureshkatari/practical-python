# mortgage.py
# Extra Payments
# Exercise 1.8
principal = 500000.0
rate = 0.05
# payment = 2684.11
total_paid = 0.0
total_months = 0

while principal > 0:
    if total_months < 12:
        payment = 2684.11 + 1000
    else:
        payment = 2684.11
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    total_months += 1

print('Total paid', total_paid)
print('Total months', total_months)