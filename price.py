has_good_credit = True
price = int(1000000)
if has_good_credit:
    down_payment = int(price) * 0.1
else:
    down_payment = int(price) * 0.2
print(f"here is the payment: {down_payment}")