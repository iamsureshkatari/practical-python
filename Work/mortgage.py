# mortgage.py
# Extra Payments
# Exercise 1.9
principal = 500000.0
rate = 0.05
total_paid = 0.0
total_months = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    payment = 2684.11
    total_months += 1
    if total_months >= extra_payment_start_month and total_months <= extra_payment_end_month:
        payment += extra_payment
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)
print('Total months', total_months)