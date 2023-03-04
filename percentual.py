#Declarando os Valores.
distribuidora = {
  "SP": 67836.43,
  "RJ": 36678.66,
  "MG": 29229.88,
  "ES": 27165.48,
  "OUTROS": 19849.53,
} 
#Calcula o percentual do total e retorna o valor em porcentagem.
def CalculaPercentual(val):
  res = (val * 100)/180759.98
  return res
#Entrada do parametro
estado = input("Estados em que é possivel Consultar\nSP\nRJ\nMG\nES\nOutros\n\nDigite o estado(Sigla) que deseja consultar percentual\n")
#Deixando os caracteres em Capslok.
estado_caps = estado.upper()
#Verificando se o valor digitado está dentro do dicionário.
if estado_caps in distribuidora:
  #Caso esteja executa.
  perce = CalculaPercentual(distribuidora[estado_caps])
  perce_round = round(perce,1)
  print(estado_caps,"teve/tiveram o fatoramento total de", distribuidora[estado_caps]," e o percentual referente ao total de vendas da distribuidora é igual a", perce_round, "%")
else:
  #Se não tiver executa essa parte e encerra o codigo.
  print("Não encontrado no dicionário")




