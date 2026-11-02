class MaxHeap:
    def __init__(self):
        # Inicializa una lista vacía para almacenar los elementos del heap
        self.heap = []

    def insert(self, element):
        # Inserta un nuevo elemento en el heap
        self.heap.append(element)
        # Ajusta el heap hacia arriba para mantener la propiedad del heap
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        # Extrae el elemento máximo del heap
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Intercambia el primer elemento (máximo) con el último y lo elimina
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        # Ajusta el heap hacia abajo para mantener la propiedad del heap
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        # Ajusta el heap hacia arriba
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            # Intercambia el elemento con su padre si es mayor
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # Llama recursivamente para seguir ajustando hacia arriba
            self._heapify_up(parent_index)

    def delete(self, element):
        # Encuentra el índice del elemento a eliminar
        try:
            index = self.heap.index(element)
        except ValueError:
            return False  # El elemento no se encuentra en el heap

        # Intercambia el elemento con el último y lo elimina
        self.heap[index] = self.heap[-1]
        self.heap.pop()

        # Ajusta el heap para mantener la propiedad del heap
        if index < len(self.heap):
            self._heapify_down(index)
            self._heapify_up(index)
        return True

    # Agrega la función a la clase MaxHeap
    MaxHeap.delete = delete