#Secuencia de Fibonacci
#@Minntcode

num1 = 0
num2 = 1
nume = int(input("ingrese el numero de veces que quiera que se repita: "))

while nume > 0:
    num1,num2 = num2, num1 + num2
    nume -= 1
    print(num1, "+", num2,"=", num1+num2)
