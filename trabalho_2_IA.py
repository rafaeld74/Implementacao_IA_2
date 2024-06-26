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

# Exemplo de uso
conjunto_total = [10, 4, 6]  # 10 exemplos da classe A, 4 da classe B e 6 da classe C
subconjuntos = [
    [6, 2, 2],  # Subconjunto para atributo = Categoria 1
    [2, 2, 2],  # Subconjunto para atributo = Categoria 2
    [2, 0, 2]   # Subconjunto para atributo = Categoria 3
]

ganho_informacao = calcular_ganho_informacao(conjunto_total, subconjuntos)
print(ganho_informacao)
