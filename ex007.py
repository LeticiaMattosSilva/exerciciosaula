def valorpagamento(valor_prestacao, dias_atraso):
    if dias_atraso == 0:
        return valor_prestacao
    else:
        # 3% do valor da prestação
        multa = valor_prestacao * 0.03
        # 0,1% por dia de atraso
        juros = valor_prestacao * (0.001 * dias_atraso)

        valor_total = valor_prestacao + multa + juros

        return valor_total

quantidade_prestacoes = 0
valor_total_dia = 0

while True:
    valor_prestacao = float(input("Digite o valor da prestação (ou 0 para sair): "))

    if valor_prestacao == 0:
        break

    dias_atraso = int(input("Digite o número de dias em atraso: "))

    # Pede para a função fazer a continha
    valor_a_pagar = valorpagamento(valor_prestacao, dias_atraso)

    # Atualiza a lista conforme for calculando (quantidade de vezes) E vai somando os valores a serem pagos
    quantidade_prestacoes += 1
    valor_total_dia += valor_a_pagar

    print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}\n")

# Mostra o que foi feito até o usuário parar.
print(f"Relatório do dia:")
print(f"Quantidade de prestações pagas: {quantidade_prestacoes}")
print(f"Valor total recebido: R$ {valor_total_dia:.2f}")
