def realizar_operacion(opcion, num1, num2):
    switch_case = {
        1: lambda: num1 + num2,  # Sumar
        2: lambda: num1 - num2,  # Restar
        3: lambda: num1 * num2,  # Multiplicar
        4: lambda: num1 / num2 if num2 != 0 else "Error: División por cero"  # Dividir
    }
    return switch_case.get(opcion, lambda: "Opción no válida")()

def main():
    while True:
        print("\nMenú de operaciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        try:
            opcion = int(input("Selecciona una opción (1-5): "))
            
            if opcion == 5:
                print("Saliendo del programa...")
                break
            
            if 1 <= opcion <= 4:
                try:
                    num1 = float(input("Introduce el primer número: "))
                    num2 = float(input("Introduce el segundo número: "))
                    resultado = realizar_operacion(opcion, num1, num2)
                    print(f"Resultado: {resultado}")
                except ValueError:
                    print("Error: Entrada inválida. Introduce números válidos.")
            else:
                print("Error: Opción no válida. Por favor, selecciona una opción entre 1 y 5.")
        
        except ValueError:
            print("Error: Entrada inválida. Debes introducir un número entre 1 y 5.")

if __name__ == "__main__":
    main()