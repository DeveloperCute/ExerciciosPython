class SelectionSort(object):

    def sort(self, data):
        if data is None:
            raise TypeError('Dados não podem ser None')
        if len(data) < 2:
            return data
        if data == []:
            return False
        self.max_num(data)
        return data
    
    def max_num(self, data):
        cont = 0
        for enum1, i1 in enumerate(data):
            aux = i1
            min_ = i1
            for i2 in range(cont, len(data)):
                if data[i2] <= min_:
                    min_ = data[i2]
                    aux = i2
            cont += 1
            print(data)
            data[enum1], data[aux] = min_, i1