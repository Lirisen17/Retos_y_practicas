lista = [
    "elemento1n1",
    "elemento2n1",
    "elemento3n1",
    [
        "elemento1n2",
        "elemento2n2",
        "elemento3n2",
        ["elemento1n3", "elemento2n3", "elemento3n3"],
    ],
]


def recorre_lista(item=[1, 2, 3, 4, 5], nivel=0):

    for x in item:
        if isinstance(x, list):
            nivel += 1
            recorre_lista(x, nivel)
        else:
            print("     " * nivel, x)


recorre_lista(lista)
