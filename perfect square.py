import math

n = int(input("Enter number: "))
root = int(math.sqrt(n))

print("Perfect Square" if root * root == n else "Not Perfect Square")
