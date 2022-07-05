def escreva(msg):
    tamanho = len(msg) + 4
    print("~" * tamanho)
    print(f'  {msg}')
    print("~" * tamanho)

mensagem = input("Digite uma palavra: ")
escreva(mensagem)