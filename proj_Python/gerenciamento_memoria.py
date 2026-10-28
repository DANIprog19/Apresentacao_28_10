def testar_anomalia_belady(paginas):
    resultados = {}

    print("\n" + "-" * 15 + " ANOMALIA DE BELADY " + "-" * 15)

    for frames in range(1, 11):
        memoria, fila = [], []
        faults = 0

        for pagina in paginas:
            if fifo(pagina, memoria, fila, frames) == "PAGE FAULT":
                faults += 1

        resultados[frames] = faults
        print(f"{frames} frames: {faults} Page Faults")

    for frames in range(1, 10):
        if resultados[frames + 1] > resultados[frames]:
            print("\n" + "-" * 15 + " ANOMALIA DETECTADA " + "-" * 15)
            print(
                f"Anomalia detectada: "
                f"{frames} para {frames + 1} frames!"
            )


def fifo(pagina, memoria, fila, qtd_frames):
    if pagina in memoria:
        return "HIT"

    if len(memoria) < qtd_frames:
        memoria.append(pagina)
        fila.append(pagina)
    else:
        antiga = fila.pop(0)
        memoria.remove(antiga)
        memoria.append(pagina)
        fila.append(pagina)
        print(f"Página substituída: {antiga} -> {pagina}")

    return "PAGE FAULT"


def lru(pagina, memoria, fila, qtd_frames):
    if pagina in memoria:
        fila.remove(pagina)
        fila.append(pagina)
        return "HIT"

    if len(memoria) < qtd_frames:
        memoria.append(pagina)
        fila.append(pagina)
    else:
        antiga = fila.pop(0)
        memoria.remove(antiga)
        memoria.append(pagina)
        fila.append(pagina)
        print(f"Página substituída: {antiga} -> {pagina}")

    return "PAGE FAULT"

paginas = [7, 0, 1, 2, 0, 3, 0, 4]

testar_anomalia_belady(paginas)