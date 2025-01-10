import threading

lock = threading.Lock()
contador = 0

def incrementar():
    global contador
    with lock:  # Bloquea el recurso
        contador += 1
        print(f"Contador: {contador}")

hilos = [threading.Thread(target=incrementar) for _ in range(5)]

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()