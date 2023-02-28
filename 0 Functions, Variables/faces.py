def convert(input):
    output = input.replace(":)","🙂" )
    output = output.replace(":(","🙁" )
    return output


def main():
    # Pedimos el input al usuario
    input_usuario = input("Place your onput here, remember the :) or the :(\n")
    # Lo pasamos a la funcion para convertirlo
    print(convert(input_usuario))


if __name__ == "__main__":
    main()