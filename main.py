def sumar(a, b):
    return a + b


def restar(a, b):
    pass


def multiplicar(a, b):
    pass


def dividir(a, b):
    if b == 0:
        return "Error: division entre cero"
    return a / b


def menu():
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def main():
    while True:
        menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "5":
            print("Hasta luego")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opcion invalida")
            continue

        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))

        if opcion == "1":
            print("Aca va la suma")
        elif opcion == "2":
            print("Aca va la resta")
        elif opcion == "3":
            print("Aca va la multiplicacion")
        else:
            resultado = dividir(a, b)

        print("Resultado:", resultado)


if __name__ == "__main__":
    main()
