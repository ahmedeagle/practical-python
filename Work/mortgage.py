principal = 500000.0
rate = 0.05
paymentExtra = 1000.0
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    months += 1
    
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        # Apply extra payment for months between 61 and 108
        interest_for_month = principal * (rate / 12)
        principal = principal + interest_for_month - (payment + paymentExtra)
        total_paid += (payment + paymentExtra)
    else:
        # Regular payment
        interest_for_month = principal * (rate / 12)
        principal = principal + interest_for_month - payment
        total_paid += payment

    print(months, round(total_paid, 2), round(principal - total_paid , 2)) 
    # Prevent overpayment if principal goes negative
    if principal < 0:
        total_paid += principal  # Adjust the total paid for any overpayment
        principal = 0
      
# Print the total paid and number of months
print('Total payment:', round(total_paid, 2), 'Number of months:', months)
