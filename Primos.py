def es_primo(n: int) -> bool:

    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 1:
            return False
        i += 6

    return True


def main():

    try:
        numero = int(input("Ingrese un número entero: "))

        if es_primo(numero):
            print(f"{numero} es primo.")
        else:
            print(f"{numero} no es primo.")

    except ValueError:
        print("Error: Debe ingresar un número entero válido.")


if __name__ == "__main__":
    main()
