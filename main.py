from decimal import Decimal

def esAprobado(nota: Decimal) -> str:
    if not isinstance(nota, (int, float, Decimal)):
        raise ValueError("La nota debe ser un número")

    nota = Decimal(nota)
    if nota < 0 or nota > 10:
        raise ValueError("La nota debe estar entre 0 y 10")

    return nota >= 5
