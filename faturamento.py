import json

# Lê o arquivo JSON com os valores de faturamento diário
with open('faturamento.json') as file:
    faturamento_diario = json.load(file)

# Calcula o menor e o maior valor de faturamento diário
min_faturamento = min(faturamento_diario)
max_faturamento = max(faturamento_diario)

# Calcula a média mensal de faturamento, ignorando os dias sem faturamento
media_mensal = sum(faturamento_diario) / len([f for f in faturamento_diario if f > 0])

# Calcula o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = len([f for f in faturamento_diario if f > media_mensal])

# Exibe os resultados
print("Menor valor de faturamento diário:", min_faturamento)
print("Maior valor de faturamento diário:", max_faturamento)
print("Número de dias com faturamento acima da média mensal:", dias_acima_da_media)