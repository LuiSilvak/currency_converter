# Conversor de Moedas em Python

Este é um projeto simples para converter valores entre moedas usando taxas de câmbio atualizadas. Ele consome uma API gratuita - Exchangerate API, para obter as taxas mais recentes.

## Funcionalidades

- Converte valores entre duas moedas.
- Atualiza automaticamente as taxas de câmbio via API.
- Interface simples baseada em terminal.

## Requisitos

- Python 3.x
- Biblioteca `requests`

Para instalar a biblioteca `requests`, execute:
```bash
pip install requests
```

## Como Usar
1. Clone o repositório
```bash
git clone https://github.com/LuiSilvak/currency_converter.git
cd currency_converter
```

2. Execute o programa:
```bash
python currency_converter.py
```

3. Siga as instruções no terminal para realizar a conversão


## Exemplo de Execução
```bash
=== Conversor de Moedas ===
Digite a moeda de origem (ex: USD): USD
Digite a moeda de destino (ex: BRL): BRL
Digite o valor a ser convertido: 100

Obtendo taxa de câmbio...
100 USD equivale a 526.30 BRL
```

## Melhorias Futuras
- Suporte a múltiplas APIs para maior robustez.
- Adicionar histórico de conversões.
- Desenvolver uma interface gráfica amigável.

## Licença
Este projeto está licenciado sob a MIT License.

