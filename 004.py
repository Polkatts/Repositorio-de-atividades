from random import randint 

def rolagem(lados, bonus=0):
    valor_dado = randint(1,lados)
    total = valor_dado + bonus

    return {
        "rolagem": valor_dado,
        "bonus": bonus,
        "total": total,
        "texto": f"{valor_dado} + {bonus} = {total}"
    }

try:
    entrada_dado = input("Insira qual dado quer rolar (Ex: d20, d12):\n>>> ").replace("d", "").strip()
    lados = int(entrada_dado)

    tem_bonus = input("Possui algum bonus? (s/n)\n>>> ").lower().strip()

    valor_bonus = 0
    if tem_bonus.startswith("s"):
        valor_bonus = int(input("Insira a quantidade do bonus:\n>>> "))

    resultado = rolagem(lados, valor_bonus)

    print(f"\nResultado: {resultado['texto']}")

except ValueError:
    print("\n [Erro] Por favor, insira apenas números válidos (ex: 20 ou d20).")
