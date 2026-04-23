# Currency Converter (Fixed rates)
rates = {"USD": 1, "EUR": 0.92, "GBP": 0.79, "JPY": 149.5, "INR": 83.1}
print("Available currencies:", ', '.join(rates.keys()))
from_cur = input("Convert FROM: ").upper()
to_cur = input("Convert TO: ").upper()
amount = float(input("Amount: "))
if from_cur in rates and to_cur in rates:
    result = amount / rates[from_cur] * rates[to_cur]
    print(f"{amount} {from_cur} = {result:.2f} {to_cur}")
else:
    print("Invalid currency code")
