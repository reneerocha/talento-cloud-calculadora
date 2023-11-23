numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")
print(" 1. Soma\n 2. Subtração\n 3. Multiplicação\n 4. Divisão")
operacao = int(input("Digite a operacao desejada: "))

if operacao == 1:
	resultado = int(numero1) + int(numero2)
elif operacao == 2:
	resultado = int(numero1) - int(numero2)
elif operacao == 3:
	resultado = int(numero1) * int(numero2)
elif operacao == 4:
	resultado = int(numero1) / int(numero2)
else:
	resultado = 0
    
print("O resultado da operação é: " + str(resultado))
