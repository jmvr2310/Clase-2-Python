
def nombre(name):
    
    print(f"Asi que te llamas {name}")

nombre(input("Como te llamas?: "))


def suma(n1, n2):
    result = n1 + n2
    return result

def resta(n1, n2):
    result = n1 - n2
    return result

print(resta(32, 28))
print(resta(20, 12))
print(suma(7, 4))

def meth(num1, num2):
    result = (f"{suma(num1, num2)}, {resta(num1, num2)}")
    return result


num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

print(f"{suma(num1, num2)}, {resta(num1, num2)}")
print(meth(num1, num2))

