print('\n')
print("-=-=-" * 20)

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

pessoas = []
i = 0
cadastrar = int(input('Quantas vezes quer cadastrar? '))

for i in range (cadastrar):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    peso = float(input('Digite o peso em kg: '))
    altura = float(input('Digite a altura em metros: '))
    imc = calcular_imc(peso, altura)

    print('\n')
    print(f' Nome: {nome}\n Idade: {idade} anos\n Peso: {peso}kg\n Altura: {altura}m \n IMC: {imc:.2f}')
    print('\n')
    if imc < 18.5:
        print(' Abaixo do peso')
    elif 18.5 <= imc < 24.9:
        print(' Peso normal')
    elif 24.9 <= imc < 29.9:
        print(' Sobrepeso')
    elif 30 <= imc <34.9:
        print(' Obesidade Grau I')
    elif 35 <= imc <= 39.9:
        print(' Obesidade Grau II')
    else:
        print(' Obesidade Grau III')
    
    cadastro = (nome, idade, peso, altura)
    pessoas.append(cadastro)

print('\n')