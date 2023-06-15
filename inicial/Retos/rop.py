"""
 * Reto #36
 * LOS ANILLOS DE PODER
 * Fecha publicación enunciado: 06/09/22
 * Fecha publicación resolución: 14/09/22
 * Dificultad: MEDIA
 *
 * Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales a Sauron
 * contra otras bondadosas que no quieren que el mal reine sobre sus tierras.
 * Cada raza tiene asociado un "valor" entre 1 y 5:
 * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3), Númenóreanos (4), Elfos (5)
 * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2), Huargos (3), Trolls (5)
 * Crea un programa que calcule el resultado de la batalla entre los 2 tipos de ejércitos:
 * - El resultado puede ser que gane el bien, el mal, o exista un empate. Dependiendo de la
 *   suma del valor del ejército y el número de integrantes.
 * - Cada ejército puede estar compuesto por un número de integrantes variable de cada raza.
 * - Tienes total libertad para modelar los datos del ejercicio.
 * Ej: 1 Peloso pierde contra 1 Orco, 2 Pelosos empatan contra 1 Orco, 3 Pelosos ganan a 1 Orco.
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
"""

VALOR_PELOSOS = 1
VALOR_SURENIOS_BUENOS = 2
VALOR_ENANOS = 3
VALOR_NUMENOREANOS = 4
VALOR_ELFOS = 5
VALOR_SURENIOS_MALOS = 2
VALOR_ORCOS = 2
VALOR_GOBLINS = 2
VALOR_HUARGOS = 3
VALOR_TROLLS = 5

ejercito = 3
total_buenos = 0
total_malos = 0


def ejercito_bueno(
    VALOR_PELOSOS, VALOR_SURENIOS_BUENOS, VALOR_ENANOS, VALOR_NUMENOREANOS, VALOR_ELFOS
):
    pelosos = int(input("Ingresar la cantidad de pelosos: ")) * VALOR_PELOSOS
    surenios_buenos = (
        int(input("Ingresar la cantidad de sureños buenos: ")) * VALOR_SURENIOS_BUENOS
    )
    enanos = int(input("Ingresar la cantidad de Enanos: ")) * VALOR_ENANOS
    numenoreanos = (
        int(input("Ingresar la cantidad de Numenoreanos: ")) * VALOR_NUMENOREANOS
    )
    elfos = int(input("Ingresar la cantidad de Elfos: ")) * VALOR_ELFOS
    total_buenos = elfos + numenoreanos + enanos + surenios_buenos + pelosos
    return total_buenos


def ejercito_malo(
    VALOR_SURENIOS_MALOS, VALOR_ORCOS, VALOR_GOBLINS, VALOR_HUARGOS, VALOR_TROLLS
):
    surenios_malos = (
        int(input("Ingresar la cantidad de sureños malos: ")) * VALOR_SURENIOS_MALOS
    )
    orcos = int(input("Ingresar la cantidad de Orcos: ")) * VALOR_ORCOS
    goblins = int(input("Ingresar la cantidad de Goblins: ")) * VALOR_GOBLINS
    huargos = int(input("Ingresar la cantidad de Huargos: ")) * VALOR_HUARGOS
    trolls = int(input("Ingresar la cantidad de Trolls: ")) * VALOR_TROLLS
    total_malos = surenios_malos + orcos + goblins + huargos + trolls
    return total_malos


print("Vamos a armar los ejercitos! ")

print("Empecemos con los buenos!")
total_buenos = ejercito_bueno(
    VALOR_PELOSOS,
    VALOR_SURENIOS_BUENOS,
    VALOR_ENANOS,
    VALOR_NUMENOREANOS,
    VALOR_ELFOS,
)

print("Listo! ahora es el turno de los malos!")
total_malos = ejercito_malo(
    VALOR_SURENIOS_MALOS,
    VALOR_ORCOS,
    VALOR_GOBLINS,
    VALOR_HUARGOS,
    VALOR_TROLLS,
)


print("La suma del ejercito bueno es de:", total_buenos)
print("La suma del ejercito malo es de:", total_malos)

if total_buenos > total_malos:
    print("ganadores los buenos")
elif total_buenos < total_malos:
    print("ganadores los malos")
else:
    print("Hay empate!")
