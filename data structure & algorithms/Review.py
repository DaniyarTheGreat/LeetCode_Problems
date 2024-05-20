class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(array_size)]

    def hash(self, key, count_collision = 0):
        key_bytes = key.encode()
        return (sum(key_bytes) + count_collision) % self.array_size
    
    def assign(self, key, value):
        array_index = self.hash(key)
        current_array_value = self.array[array_index]
        if current_array_value is None:
            self.array[array_index] = [key, value]
            return
        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return
        number_collisions = 1
        while current_array_value[0] != key:
            new_array_index = self.hash(key, number_collisions)
            current_array_value = self.array[new_array_index]
            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return
            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return
            number_collisions += 1
        return

    def retrieve(self, key):
        index = self.hash(key)
        possible_return_value = self.array[index]
        if possible_return_value is None:
            return None
        if possible_return_value[0] == key:
            return possible_return_value[1]
        retrieval_collisions = 1
        while possible_return_value[0] != key:
            retrieving_array_index = self.hash(key, retrieval_collisions)
            retrieval_collisions += 1
            if self.array[retrieving_array_index] is None:
                return None
            if self.array[retrieving_array_index][0] != key:
                retrieval_collisions += 1
            else:
                return possible_return_value[1]
        return