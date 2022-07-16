import random


def elegir_palagra():
    with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        palabras = [line for line in f]
    palabra = palabras[random.randint(0, len(palabras))]
    palabra_oculta = {i: '_'for i in range(len(palabra)-1)}
    sin_acentos = palabra.maketrans('áéíóú', 'aeiou')
    palabra = palabra.translate(sin_acentos)
    return palabra, palabra_oculta


def interfaz():
    print('Bienvenido al juego del ahorcado')
    print('---------------------------------')


def revelar_palabra(palabra, palabra_oculta):
    letra = solicitar_letra()
    if letra in palabra:
        indices = [pos for pos, char in enumerate(palabra) if char == letra]
        palabra_oculta = palabra_oculta | {i: letra for i in indices}
    else:
        print('La letra no esta en la palabra')

    return palabra_oculta


def solicitar_letra():
    letra = input('Ingrese una letra: ')
    return letra


def main():
    interfaz()
    palabra, palabra_oculta = elegir_palagra()
    print(' '.join(palabra_oculta.values()))
    while '_' in ''.join(palabra_oculta.values()):
        palabra_oculta = revelar_palabra(palabra, palabra_oculta)
        print(' '.join(palabra_oculta.values()))


if __name__ == '__main__':
    main()

# NOTA: como sabemos es posible que quienes tomemos este curso basado en estos apuntes no disponemos de mucho
# tiempo, es por esto que dejo una base del reto y espero el siguiente le agregue al menos una nueva funcionalidad
# Me gustaría un sistema de vidas y uno de puntos, si gana sube un nivel si pierde baja uno.. algo así.
