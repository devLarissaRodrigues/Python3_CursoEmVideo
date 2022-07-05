def contagem(inicio, fim, passo):
    print("-=" * 20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")

    for elemento in range(inicio, fim, passo):
        print(elemento)

contagem(1, 11 , 1)
print("-=" * 20)

print("Contagem de 10 até 0 de 2 em 2")
contagem(10,-1,2)
print("-=" * 20)

print("Agora é sua vez de personalizar a contagem!")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contagem(i, f , p)
