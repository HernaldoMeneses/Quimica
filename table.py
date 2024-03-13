import pandas as pd

# Lista de listas contendo as informações de cada elemento
elementos = [
    ['Hidrogênio', 'H', 1, 1.00797],
    ['Hélio', 'He', 2, 4.0026],
    ['Lítio', 'Li', 3, 6.94],
    ['Berílio', 'Be', 4, 9.0122],
    ['Boro', 'B', 5, 10.81]
]

# Criando o DataFrame a partir da lista de listas
df = pd.DataFrame(elementos, columns=['Elemento', 'Símbolo', 'Número Atômico', 'Massa Atômica'])

# Exibindo o DataFrame
print(df)

