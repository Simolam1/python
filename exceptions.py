import sys

# x = int(input("x : "))

# y = int(input("y : "))

# result = x/y

# print(f"{x} / {y} = {result}")

try:
    u = int(input("u : "))
    v = int(input("v : "))
except ValueError:
    print("Error Valid input.")
    sys.exit(1)
    



try:
    res = u / v
except ZeroDivisionError:
    print("Error : cannot divide by 0.")
    sys.exit(1)

print(f"{u} / {v} = {res}")