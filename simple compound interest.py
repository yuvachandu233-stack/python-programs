P = float(input("Principal: "))
R = float(input("Rate: "))
T = float(input("Time: "))

SI = (P * R * T) / 100
CI = P * (1 + R/100)**T - P

print("Simple Interest:", SI)
print("Compound Interest:", CI)
