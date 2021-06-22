import os
os.system("cls")
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")


anything = input("Tell me anything...")
print("Hmm...", anything, "... Really?")

# result of the input() function is a string. this generate an error
# anything = input("Enter a number: ")
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# result of the input() function is a string. this generate an error
# anything = float(input("Enter a number: "))
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

print(-6**2)
print(-2**6)
print(-2**20)

# concatenation str + str
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

# replication str * 3, Try practicing to create other shapes or your own artwork!
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")









