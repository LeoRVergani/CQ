from datetime import datetime

def calcular_descontos(compras):
    resultado = []
    
    for data_str, valor in compras:
        data_compra = datetime.strptime(data_str, "%d/%m/%Y")
        dia = data_compra.day
        mes = data_compra.month
        ano = data_compra.year

        if 21 <= dia or dia <= 5:
            # Compra entre 21 até 05
            if dia >= 21:
                desconto_mes = mes + 1 if mes < 12 else 1
                desconto_ano = ano if mes < 12 else ano + 1
            else:
                desconto_mes = mes
                desconto_ano = ano

            saldo_reduzido_em = data_compra.strftime("%d/%m/%Y")
        else:
            # Compra entre 06 até 20
            desconto_mes = mes + 1 if mes < 12 else 1
            desconto_ano = ano if mes < 12 else ano + 1
            saldo_reduzido_em = f"21/{mes:02d}/{ano}"

        resultado.append({
            "data_compra": data_compra.strftime("%d/%m/%Y"),
            "valor": valor,
            "desconto_em": f"{desconto_mes:02d}/{desconto_ano}",
            "saldo_reduzido_em": saldo_reduzido_em
        })

    return resultado


# EXEMPLO DE USO:
compras = [
    ("25/04/2025", 100.00),
    ("04/05/2025", 80.50),
    ("10/05/2025", 60.00),
    ("18/05/2025", 40.00),
    ("22/05/2025", 120.00)
]

resultado = calcular_descontos(compras)

for item in resultado:
    print(f"Compra em {item['data_compra']} de R$ {item['valor']:.2f}")
    print(f" → Valor será descontado no mês: {item['desconto_em']}")
    print(f" → Saldo será reduzido em: {item['saldo_reduzido_em']}")
    print("---")
