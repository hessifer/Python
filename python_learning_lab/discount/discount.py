prices = input().strip().split()
prices = list(map(float, prices))
total = 0.0

for p in prices:
    total += p

if len(prices) > 6:
    discount = total * .30
elif len(prices) > 3:
    discount = total * .20
else:
    discount = total * .10

print(round(discount,1))
