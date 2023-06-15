"""/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */



 roma
 amor
 """


def es_anagrama(palabra, anagrama):
    palabra = palabra.lower()
    anagrama = anagrama.lower()

    if palabra == anagrama or len(palabra) != len(anagrama):
        return False
    coincidencias = len(palabra)

    for i in palabra:
        for e in anagrama:
            if e == i:
                coincidencias -= 1
                break

    if coincidencias == 0:
        return True
    else:
        return False


print(
    "El resultado es:",
    es_anagrama(input("ingresar palabra: "), input("Ingresar anagrama: ")),
)
