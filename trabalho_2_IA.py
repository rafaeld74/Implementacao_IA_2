import math

def calcular_entropia(proporcoes):
    
    entropia = 0
    for proporcao in proporcoes:
        if proporcao > 0:
            entropia -= proporcao * math.log2(proporcao)
    return entropia

def calcular_ganho_informacao(conjunto_total, subconjuntos):
    
    total_exemplos = sum(conjunto_total)
    proporcoes_total = [x / total_exemplos for x in conjunto_total]
    entropia_total = calcular_entropia(proporcoes_total)
    
    entropia_subconjuntos = 0
    for subconjunto in subconjuntos:
        total_subconjunto = sum(subconjunto)
        proporcoes_subconjunto = [x / total_subconjunto for x in subconjunto]
        entropia_subconjuntos += (total_subconjunto / total_exemplos) * calcular_entropia(proporcoes_subconjunto)
    
    ganho_informacao = entropia_total - entropia_subconjuntos
    return ganho_informacao

def melhor_atributo(conjunto_total, todos_subconjuntos):
    melhor_ganho = -1
    melhor_atributo = None
    
    for atributo, subconjuntos in todos_subconjuntos.items():
        ganho_informacao = calcular_ganho_informacao(conjunto_total, subconjuntos)
        print(f"Ganho de informação para {atributo}: {ganho_informacao}")
        if ganho_informacao > melhor_ganho:
            melhor_ganho = ganho_informacao
            melhor_atributo = atributo
    
    return melhor_atributo

# Exemplo de uso
conjunto_total = [10, 4, 6]  # 10 exemplos da classe A, 4 da classe B e 6 da classe C
todos_subconjuntos = {
    "Atributo1": [
        [6, 2, 2],  # Subconjunto para atributo = Categoria 1
        [2, 2, 2],  # Subconjunto para atributo = Categoria 2
        [2, 0, 2]   # Subconjunto para atributo = Categoria 3
    ],
    "Atributo2": [
        [4, 2, 4],  # Subconjunto para atributo = Categoria 1
        [4, 0, 2],  # Subconjunto para atributo = Categoria 2
        [2, 2, 0]   # Subconjunto para atributo = Categoria 3
    ]
}
melhor_atributo_selecionado = melhor_atributo(conjunto_total, todos_subconjuntos)
print(f"O melhor atributo é: {melhor_atributo_selecionado}")

#ganho_informacao = calcular_ganho_informacao(conjunto_total, subconjuntos)
#print(ganho_informacao)
