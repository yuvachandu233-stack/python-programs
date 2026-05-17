n = int(input("Enter number: "))
temp = n
digits = len(str(n))
total = 0

while temp > 0:
    d = temp % 10
    total += d ** digits
    temp //= 10

print("Armstrong" if total == n else "Not Armstrong")
