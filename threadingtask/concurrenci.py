import threading

def imprimir_mensaje(mensaje, repeticiones):
    for i in range(repeticiones):
        print(mensaje)

hilos = [
    threading.Thread(target=imprimir_mensaje, args=("Hilo 1", 5)),
    threading.Thread(target=imprimir_mensaje, args=("Hilo 2", 5))
]

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todas las tareas han finalizado")
