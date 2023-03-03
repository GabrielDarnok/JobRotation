# Função que calcula a sequência de Fibonacci até um determinado valor n
def VerificaFib(n):
  # Inicia a sequência com 0 e 1
    fib = [0, 1]
    # Adiciona os próximos valores da sequência até n
    while fib[-1] < n:
      fib.append(fib[-1] + fib[-2])
    # Retorna a sequência
    return fib
#Solicitando o valor de entrada para comparar com a sequencia fib
num = int(input("Digite um numero para verificar se faz parte da sequêcia de Fibonacci: "))
#Chamando a função que vai fazer a verificação
seq_fib = VerificaFib(num)

print("---" *18)
#Printando o resultado referente a comparação
if num in seq_fib:
  print("O numero ", num ," faz parte da sequencia ", seq_fib)
else:
  print("O numero ", num ,"Não faz parte da sequencia ",seq_fib)