# Importando biblioteca
import requests


def get_exchange_rate(base_currency, target_currency):
    """Obtém a taxa de câmbio entre duas moedas."""
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        if target_currency in data["rates"]:
            return data["rates"][target_currency]
        else:
            print(f"Erro: Moeda {target_currency} não encontrada.")
            return None
    except Exception as e:
        print(f"Erro ao acessar a API: {e}")
        return None

   
def convert_currency(amount, rate):
    """Converte um valor de acordo com a taxa de câmbio."""
    return amount * rate


def main():
    print("=== Conversor de Moedas ===")
    base_currency = input("Digite a moeda de origem (ex: USD): ").upper()
    target_currency = input("Digite a moeda de destino (ex: BRL): ").upper()
    amount = float(input("Digite o valor a ser convertido: "))

    print("\nObtendo a taxa de câmbio...")
    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate:
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"{amount} {base_currency} equivale a {converted_amount:.2f} {target_currency}")
    else:
        print("Não foi possível realizar a conversão.")


if __name__ == "__main__":
    main()