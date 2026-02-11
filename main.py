import random


def ler_conjunto_usuario():
    A = set()

    print("Digite numeros inteiros de 0 a 20 para compor o conjunto A")
    print("Mínimo: 4 | Máximo: 8")
    print("Pressione ENTER sem digitar nada para encerrar\n")

    while True:
        if len(A) == 8:
            print("Tamanho máximo atingido.")
            break

        entrada = input(f"Elemento {len(A) + 1}: ").strip()

        if entrada == "":
            if len(A) >= 4:
                break
            else:
                print("O conjunto precisa ter pelo menos 4 elementos.")
                continue

        try:
            num = int(entrada)
        except ValueError:
            print("Digite apenas números inteiros.")
            continue

        if num < 0 or num > 20:
            print("Digite um número entre 0 e 20.")
        elif num in A:
            print("Elemento repetido! Digite outro.")
        else:
            A.add(num)

    return A


def gerar_conjunto_aleatorio():
    B = set()
    tam = random.randint(4, 8)

    while len(B) < tam:
        num = random.randint(0, 20)
        B.add(num)

    return B


def criar_universo():
    return set(range(21))


def mostrar_resultados(A, B, U):
    print("\n" + "="*40)
    print("CONJUNTOS")
    print("="*40)
    print("Conjunto A (usuário):", A)
    print("Conjunto B (aleatório):", B)
    print("Conjunto Universo U:", U)

    print("\n" + "="*40)

    print("CARDINALIDADES")
    print("="*40)
    print("|A| =", len(A))
    print("|B| =", len(B))
    print("|A ∪ B| =", len(A | B))
    print("|A ∩ B| =", len(A & B))

    print("\n" + "="*40)

    print("OPERAÇÕES")

    print("="*40)

    print("A ∪ B =", A | B)
    intersecao = A & B
    print("A ∩ B =", intersecao if intersecao else "∅ (Vazio)")
    print("A - B =", A - B)
    print("B - A =", B - A)
    print("A Δ B =", A ^ B)
    print("A^c =", U - A)
    print("B^c =", U - B)


# ---------- PROGRAMA PRINCIPAL ----------

A = ler_conjunto_usuario()
B = gerar_conjunto_aleatorio()
U = criar_universo()

mostrar_resultados(A, B, U)
