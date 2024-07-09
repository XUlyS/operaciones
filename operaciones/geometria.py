# geometria.py

import math

def area_circulo(radio):
    """Devuelve el área de un círculo dado su radio."""
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    return math.pi * radio ** 2

def perimetro_circulo(radio):
    """Devuelve el perímetro de un círculo dado su radio."""
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    return 2 * math.pi * radio

def area_rectangulo(base, altura):
    """Devuelve el área de un rectángulo dada su base y altura."""
    if base < 0 or altura < 0:
        raise ValueError("La base y la altura no pueden ser negativas.")
    return base * altura

def perimetro_rectangulo(base, altura):
    """Devuelve el perímetro de un rectángulo dada su base y altura."""
    if base < 0 or altura < 0:
        raise ValueError("La base y la altura no pueden ser negativas.")
    return 2 * (base + altura)
