modelos = ["Fusca", "Gol", "Uno", "Vectra", "Peugeout"]
consumo = [7, 10, 12.5, 9, 14.5,]
preco_gasolina = 2.25

# A função min(consumo) encontra o valor mínimo na lista consumo(menor consumo entre todos os carros).
# O método .index(min(consumo)) encontra o índice desse valor mínimo na lista consumo
# O resultado desse cálculo é atribuído à variável indice_mais_economico.
indice_mais_economico = consumo.index(min(consumo))

print(f"Modelo mais econômico: {modelos[indice_mais_economico]}")

for i in range(len(modelos)):
    consumo_1000_km = 1000 / consumo[i] #Aramazena na lista consumo_1000_km  quantos litros de gasolina os carros precisam.
    custo = consumo_1000_km * preco_gasolina #calcula o custo da gasolina necessária.
    print(f"{modelos[i]} consome {consumo_1000_km:.2f} litros e custa R$ {custo:.2f}")
