import os
os.system('cls')

# input without argument
print("Tell me anything...")
anything = input() 
print("Hmm...", anything, "... Really?")

# input with argument
anything = input("Tell me anything...") # anything is a str
print("Hmm...", anything, "... Really?")
print(type(anything))

# str to float
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# pitagorean theorem (don't react to negative values)
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)


start = int(input("Input the first number: "))
end = int(input("Input the second number: "))

s = start
e = start + 1
while e < (end + 1):
    s = s + e
    e += 1
print(s)
sumatoria = end * (end + 1) / 2
print(sumatoria)


