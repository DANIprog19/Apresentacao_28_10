
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

print("\n" + "-" * 20 + " SIMULAÇÃO DE PAGINAÇÃO " + "-" * 20)

qtd_frames = int(input("\nDigite a quantidade de frames: "))

print("-" * 55)

memoria = []
fila = []
faults = 0
hits = 0

print("\n" + "-" * 25 + " FIFO " + "-" * 25)

for pagina in paginas:
    resultado = fifo(pagina, memoria, fila, qtd_frames)

    if resultado == "HIT":
        hits += 1
    else:
        faults += 1

    print(
        f"Página: {pagina} - Resultado: {resultado} "
        f"- Memória: {memoria} - Fila: {fila}"
    )

print(f"\nHits: {hits}")
print(f"Page Faults: {faults}")

print("\n" + "-" * 25 + " LRU " + "-" * 25)

memoria = []
fila = []
hits = 0
faults = 0

for pagina in paginas:
    resultado = lru(pagina, memoria, fila, qtd_frames)

    if resultado == "HIT":
        hits += 1
    else:
        faults += 1

    print(
        f"Página: {pagina} - Resultado: {resultado} "
        f"- Memória: {memoria} - Fila: {fila}"
    )

print(f"\nHits: {hits}")
print(f"Page Faults: {faults}")


print("\n" + "-" * 20 + " RESULTADO FINAL " + "-" * 20)
print(f"Hits: {hits}")
print(f"Page Faults: {faults}")

print("\n" + "-" * 20 + " FIM DA SIMULAÇÃO " + "-" * 20)