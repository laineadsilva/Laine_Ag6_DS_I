# Sistema de Desconto Progressivo
# Agenda 06 - Desenvolvimento de Sistemas I
# Aluna: Laíne Adriéle da Silva Moraes

# Solicita ao usuário o valor total da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verifica a faixa de desconto de acordo com o valor da compra
if valor_compra < 200:
    percentual_desconto = 0.05
elif valor_compra < 300:
    percentual_desconto = 0.10
else:
    percentual_desconto = 0.15

# Calcula o valor do desconto e o valor final da compra
valor_desconto = valor_compra * percentual_desconto
valor_final = valor_compra - valor_desconto

# Exibe o resultado
print("\n--- RESUMO DA COMPRA ---")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {percentual_desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_final:.2f}")