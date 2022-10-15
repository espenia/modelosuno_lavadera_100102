import random
import threading


def do_e(row, graphs):
    values = []
    current = ""
    for col in row:
        if col != " " and col != "e":
            current += col
        elif col == " " and current != "":
            values.append(int(current))
            current = ""
    values.append(int(current))
    if values[0] not in graphs:
        graphs[values[0]] = []
    if values[1] not in graphs:
        graphs[values[1]] = []
    if values[1] not in graphs[values[0]]:
        graphs[values[0]].append(values[1])
    if values[0] not in graphs[values[1]]:
        graphs[values[1]].append(values[0])
    return graphs


def identify(tipo, row, graph):
    if tipo == "e":
        graph = do_e(row, graph)
    return graph


def cargar_matriz(route, graph):
    file = open(route, "r")
    for r in file:
        graph = identify(r[0], r, graph)
    file.close()
    return graph


def multi_threading(graph):
    global tandas_finales
    tandas_finales = []
    threads = []
    for i in range(0, 500):
        t = threading.Thread(target=setup_tandas, args=[graph])
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    tanda_final = []
    for tanda in tandas_finales:
        if len(tanda_final) == 0:
            tanda_final = tanda
        elif len(tanda) < len(tanda_final):
            print("final " + str(len(tanda)) + "\t")
            tanda_final = tanda
    return tanda_final


def setup_tandas(graph):
    tandas = []
    tandas_temp = []
    skip = []
    items = list(graph.items())

    for i in range(0, 10000):
        random.shuffle(items)
        for item in items:
            lavar = [item[0]]
            if item[0] in skip:
                continue
            for item2 in items:
                if item[0] != item2[0] and item2[0] not in item[1] and item2[0] not in skip:
                    any_present = False
                    for value in item2[1]:
                        if value in lavar:
                            any_present = True
                            break
                    if not any_present:
                        lavar.append(item2[0])
                        skip.append(item2[0])
            skip.append(item[0])
            tandas_temp.append(lavar)
        if len(tandas) == 0:
            tandas = tandas_temp
        elif len(tandas_temp) < len(tandas):
            tandas = tandas_temp
    tandas_finales.append(tandas)
    return tandas


def program():
    graph = {}
    graph = cargar_matriz("tercer_problema.txt", graph)
    tandas = multi_threading(graph)
    print(tandas)
    f = open("entrega_3.txt", "w")
    for i in range(0, len(tandas)):
        for value in tandas[i]:
            f.write(str(value) + " " + str(i + 1) + "\n")
    f.close()


program()
