produtos = []
i = 0
cadastrar = int(input('Quantos produtos deseja cadastrar? '))

for i in range(cadastrar):
    nome = input('Digite o nome do produto: ')
    quantidade = int(input('Digite a quantidade: '))
    valor = float(input('Digite o valor: R$ '))
    pago = float(input('Digite o valor cobrado: R$ '))

    if pago > valor:
        print(f'Você pagou {pago} mas o {nome} custa {valor}.\n Seu troco é de R${pago - valor:.2f}')

    cadastro = (nome, quantidade, valor)
    produtos.append(cadastro)

print(produtos)

 




