# print()
# print(" Hello R, HELP ME!!!!" * 2)
# print(24 * 45)
# print("my","name","is","yober",end=" is full name",sep="-")
# print("Hello, MOM\n" * 10)

print("Alemania\nEspaña\nItalia")
print()
print()
print()
print("Francia\nInglaterra\nURSS")
print("\\")
print("hola","me llamo","yober\n")
print("my name is ", end="yober y no es eso de ")
print("Monty python.")
print("hola","me","llamo","yober",sep="-")
print("hola","me","llamo","yober",sep=" # ")
print("Alemania","España","Italia",sep=" ")

print("beautiful","face","eyes",sep="121",end=" aqui termina\n")
print("kioc",12,False,"feo",sep="XD",end=" aqui voy\n")

print("-----------------------------\n")

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print(("  *   *\n" * 6),end="")
print("  *****")

print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *   *\n  *   *\n  *   *\n  *   *\n  *   *\n  *****")
print()
print('  *****   ')
print('  *****   ')
print("All the people")


a = 12_345
b = 2_324_567
print(a + b)

a = -12_345
b = 2_324_567
print(a + b)
print("------------------")



num = float(input("Ingresa el numero: "))
sis = int(input("A que sistema? "))
op = "True"
lista = []
while op == "True":
    resto = num % sis
    lista.append(resto)
    if num // sis < sis:
        lista.append(1)
        op = "False"
    else:
        num = num // sis
lista.reverse()
print(lista)


