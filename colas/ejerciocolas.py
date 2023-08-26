from collections import deque

list_new = ["hector", "juan", "maria", "pedro"]

cola = deque()

for i in list_new:
    cola.append(i)

print(cola)