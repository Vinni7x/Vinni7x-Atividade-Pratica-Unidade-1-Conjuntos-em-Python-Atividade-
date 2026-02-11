# Atividade – Operações com Conjuntos em Python

Disciplina: Lógica e Matemática Discreta (EECP0015)  
Curso: Engenharia da Computação – UFMA  
Professor: Prof. Rondineli Seba  
Discente: Marcos Vinícius Jansem Oliveira 
Matrícula: 20250071278

## Objetivo da Atividade

  · Aplicar os conceitos de teoria dos conjuntos (união, interseção, diferença, complemento, cardinalidade etc.) em um programa em Python ou na linguagem de sua preferência.

  · Desenvolver boas práticas de organização de código, uso de funções e documentação.

##  Descrição do Problema

O programa trabalha com dois conjuntos:

  - **Conjunto A**: definido pelo usuário.
  - **Conjunto B**: gerado aleatoriamente pelo programa.

### Requisitos implementados:

1. O usuário deve informar entre **4 e 8 números inteiros**.
   - Caso deseje finalizar antes de atingir 8 elementos, pode pressionar Enter sem digitar nenhum valor (desde que já tenha informado pelo menos 4 elementos).
3. Os números devem estar no intervalo de **0 a 20**.
4. O programa valida:
   - Quantidade mínima e máxima
   - Elementos repetidos
   - Valores fora do intervalo
   - Entradas inválidas (não numéricas)
5. O segundo conjunto (B) é gerado aleatoriamente, também com:
   - Entre 4 e 8 elementos
   - Valores no intervalo de 0 a 20
6. Foi definido um conjunto universo:
   - U = {0, 1, 2, ..., 20}
  
##  Como Executar o Programa

### Pré-requisitos

- Python 3 instalado (versão 3.x)
- Não é necessário instalar bibliotecas externas (usa apenas `random`, que já faz parte do Python)

###  Executando pelo terminal

1. Baixe ou clone o repositório:
   ```bash
   git clone https://github.com/Vinni7x/Vinni7x-Atividade-Pratica-Unidade-1-Conjuntos-em-Python-Atividade-
2. Acesse a pasta:

  -cd Vinni7x-Atividade-Pratica-Unidade-1-Conjuntos-em-Python-Atividade


3. Execute o programa:

  -python main.py

##  Organização do Código

O programa foi estruturado utilizando funções, separando responsabilidades para melhor organização e legibilidade.

###  `ler_conjunto_usuario()`

Responsável por:

- Ler os valores digitados pelo usuário  
- Validar entradas  
- Garantir que o conjunto tenha entre 4 e 8 elementos  
- Retorna o conjunto A  

Essa função demonstra boas práticas como:

- Tratamento de exceções (`try/except`)  
- Validação de dados  
- Controle de fluxo com `while`  

---

###  `gerar_conjunto_aleatorio()`

- Gera o conjunto B  
- Define aleatoriamente o tamanho entre 4 e 8  
- Garante que os valores estejam no intervalo permitido  

Utiliza:

- `random.randint()`  
- Estrutura de repetição  
- Propriedade de conjuntos (não permite repetição automática)  

---

###  `criar_universo()`

Cria o conjunto universo:

```
U = {0, 1, ..., 20}
```

Utiliza:

```python
set(range(21))
```

---

###  `mostrar_resultados(A, B, U)`

Responsável por:

- Mostrar os conjuntos  
- Calcular e exibir:

  - União (A ∪ B)  
  - Interseção (A ∩ B)
    -Para o conjunto Vazio: O programa identifica quando a interseção é nula e exibe o símbolo $\emptyset$ em vez de set(), facilitando a leitura humana. 
  - Diferença (A - B)  
  - Diferença (B - A)  
  - Diferença Simétrica (A Δ B)  
  - Complemento (Aᶜ e Bᶜ)  
  - Cardinalidades (|A|, |B|, |A ∪ B|, |A ∩ B|)  

Organiza a saída de forma clara e legível.

---

##  Relação com os Conceitos de Teoria dos Conjuntos

O programa aplica diretamente os conceitos vistos em sala:

###  União (A ∪ B)

Implementado com:

```python
A | B
```

Reúne todos os elementos de A e B sem repetição.

---

###  Interseção (A ∩ B)

Implementado com:

```python
A & B
```

Mostra os elementos comuns entre A e B.

---

###  Diferença (A - B)

Implementado com:

```python
A - B
```

Mostra os elementos que pertencem a A mas não pertencem a B.

---

###  Diferença Simétrica (A Δ B)

Implementado com:

```python
A ^ B
```

Mostra os elementos que pertencem a apenas um dos conjuntos.

---

###  Complemento (Aᶜ)

Implementado com:

```python
U - A
```

Mostra os elementos do universo que não pertencem ao conjunto A.

---

###  Complemento (Bᶜ)

Implementado com:

```python
U - B
```

Mostra os elementos do universo que não pertencem ao conjunto B.

---

###  Cardinalidade

Implementado com:

```python
len(A)
```

Representa o número de elementos do conjunto.





