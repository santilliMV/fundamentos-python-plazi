x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

y_str = format(y, ".2g") #forma gramatica
print("str", y_str)
print(y_str == str(x))

print("*" * 10)

print(y, x)

tolerance = 0.00001
print(abs(x - y) < tolerance) #forma matematica

print(round(y, 1)) #forma facil
print(x == round(y,1))
