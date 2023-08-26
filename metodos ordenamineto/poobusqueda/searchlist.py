
class Order:
    
    def __init__(self, list_ordering):
        self.list_ordering = list_ordering

    def bubble_order(self):
        for i in range(len(self.list_ordering)):
            for j in range(len(self.list_ordering)-1):
                if self.list_ordering[j] > self.list_ordering[j+1]:
                    aux = self.list_ordering[j]
                    self.list_ordering[j] = self.list_ordering[j+1]
                    self.list_ordering[j+1] = aux
        return self.list_ordering
    
    def merge(self, list_left,list_right):
        index_array_order = 0
        index_left = 0
        index_right = 0
        array_order = []

        while(index_left < len(list_left) and index_right < len(list_right)):
            if list_left[index_left] < list_right[index_right]:
                array_order.append(list_left[index_left])
                index_left += 1
            else:
                array_order.append(list_right[index_right])
                index_right += 1
            index_array_order += 1

        while(index_left < len(list_left)):
            array_order.append(list_left[index_left])
            index_left += 1

        while(index_right < len(list_right)):
            array_order.append(list_right[index_right])
            index_right += 1
        
        return array_order
    
    def merge_sort(self):
        if len(self.list_ordering) < 2:
            return self.list_ordering
        
        else:
            middle = len(self.list_ordering) // 2
            right = Order(self.list_ordering[middle:])
            left = Order(self.list_ordering[:middle])
            return self.merge(right.merge_sort(), left.merge_sort())
        
    def order_incert(self):
        for i in range(len(self.list_ordering)):
            pos = i
            aux = self.list_ordering[i]

            while (pos > 0) and (self.list_ordering[pos-1] > aux):
                self.list_ordering[pos] = self.list_ordering[pos-1]
                pos -= 1
                self.list_ordering[pos] = aux
        return self.list_ordering
    
    def order_select(self):
        for i in range(len(self.list_ordering)):
            min = i
            for j in range(i + 1, len(self.list_ordering)):
                if self.list_ordering[j] < self.list_ordering[min]:
                    min = j
            
            aux = self.list_ordering[i]
            self.list_ordering[i] = self.list_ordering[min]
            self.list_ordering[min] = aux
        return self.list_ordering



class Search:

    def __init__(self, list_search):
        self.list_search = []


lista = [3, 8, 1, 6, 2, 4] 

ordenar_lista = Order(lista)
#print(ordenar_lista.bubble_order())
#print(ordenar_lista.merge_sort())
#print(ordenar_lista.order_incert())
print(ordenar_lista.order_select())