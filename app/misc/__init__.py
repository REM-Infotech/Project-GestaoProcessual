import unicodedata

import babel.numbers as numbers
from iso3166 import countries
from phonenumbers import (
    PhoneNumberFormat,
    country_code_for_region,
    format_number,
    parse,
)

# from babel.dates import format_date


def format_currency_brl(value) -> str:

    number = numbers.format_currency(value, "BRL", locale="pt_BR")
    number = unicodedata.normalize("NFKD", number)
    return number


def gerar_sigla(nome_cliente):
    # Palavras a serem ignoradas
    palavras_ignoradas = ["LTDA", "S/A", "EIRELI"]

    # Separar o nome da cliente em palavras e filtrar as palavras a serem ignoradas
    palavras = [
        palavra
        for palavra in nome_cliente.upper().split()
        if palavra not in palavras_ignoradas
    ]

    # Coletar as duas primeiras letras de cada palavra
    letras = [palavra[:2] for palavra in palavras if len(palavra) > 1]

    # Concatenar as letras e limitar a 3 caracteres
    sigla = "".join(letras)[:3]

    return sigla


def formatar_numero(numero: str) -> str:

    ddi = None
    if "+" not in numero:
        return None

    for country in countries:
        if f"{country_code_for_region(country.alpha2)}" in numero:
            ddi = f"+{country_code_for_region(country.alpha2)}"

    if not ddi:
        return None

    phone_number = parse(numero.replace(" ", ""))
    return format_number(phone_number, PhoneNumberFormat.INTERNATIONAL)
