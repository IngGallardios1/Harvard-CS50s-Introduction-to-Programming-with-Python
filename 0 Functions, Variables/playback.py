import math


def main():
    # Input del texto del usuario
    input_usuario = input()
    # Reemplazamos los espacios por "..."
    input_usuario = input_usuario.replace(" ", "...")
    # imprimimos el input del usuario
    print(input_usuario)


if __name__ == '__main__':
    main()