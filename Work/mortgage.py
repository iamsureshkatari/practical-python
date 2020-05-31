# mortgage.py
# Extra Payments
# Exercise 1.10
# month, total paid, remaining principal
principal = 500000.0
rate = 0.05
total_paid = 0.0
month = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    payment = 2684.11
    month += 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        payment += extra_payment
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print(month, total_paid, principal)

print('Total paid', total_paid)
print('Total months', month)