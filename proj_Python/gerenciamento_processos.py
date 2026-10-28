import threading
import time

recurso_1 = threading.Lock()
recurso_2 = threading.Lock()


def processo_a():
    print("[Processo A] Executando...")

    with recurso_1:
        print("[Processo A] Adquiriu o Recurso 1.")

        time.sleep(1)

        print("[Processo A] Aguardando o Recurso 2...")

        with recurso_2:
            print("[Processo A] Adquiriu o Recurso 2.")


def processo_b():
    print("[Processo B] Executando...")

    with recurso_2:
        print("[Processo B] Adquiriu o Recurso 2.")

        time.sleep(1)

        print("[Processo B] Aguardando o Recurso 1...")

        with recurso_1:
            print("[Processo B] Adquiriu o Recurso 1.")


print("\n" + "-" * 20 + " SIMULAÇÃO DE DEADLOCK " + "-" * 20)

a = threading.Thread(target=processo_a, daemon=True)
b = threading.Thread(target=processo_b, daemon=True)

a.start()
b.start()

a.join(timeout=3)
b.join(timeout=3)

if a.is_alive() or b.is_alive():
    print("\n[!] DEADLOCK DETECTADO!")
    print("Processos envolvidos: Processo A e Processo B.")
    print("Processo A aguarda o Recurso 2.")
    print("Processo B aguarda o Recurso 1.")
else:
    print("\nProcessos finalizados sem deadlock.")

print("-" * 60)