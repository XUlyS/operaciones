# main.py
# Autor: Danilo
# Fecha: 8 de julio de 2024
# Versión: 1
import operaciones.matematica as mat
import operaciones.geometria as geo

def main():
    try:
        print(f"Multiplicación (10 * 5): {mat.multiplicacion(10, 5)}")
        print(f"División (10 / 5): {mat.division(10, 5)}")
        print(f"Área del rectángulo (10 * 5): {geo.area_rectangulo(10, 5)}")
        print(f"Perímetro del rectángulo (10, 5): {geo.perimetro_rectangulo(10, 5)}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
