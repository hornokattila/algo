class Merge:
    def __init__(self, array):
        self.array = array
        print("I: {}".format(self.array))
        # Turns true for processed indexes.
        self.debug = [False for _ in range(len(array))]

    def _calculate_shift(self, index):
        if index < round((len(self.array) + .5) / 2):
            return index
        else:
            _parity_coefficient = 1 if len(self.array) % 2 == 0 else 0
            return -self._calculate_shift(len(self.array) - index - _parity_coefficient)

    def _calculate_new_index(self, index):
        return index + self._calculate_shift(index)

    def _calculate(self, index, value):
        _forward_index = self._calculate_new_index(index)
        _forward_value = self.array[_forward_index]
        print("index: {}, value: {} -> forward index: {} | (forward value: {})"
              .format(index, value, _forward_index, _forward_value))
        self.array[_forward_index] = value
        self.debug[_forward_index] = True
        if _forward_value:
            self._calculate(_forward_index, _forward_value)

    def calculate(self):
        if len(merge.array) > 2:
            value = self.array[1]
            self.array[1] = None
            self._calculate(1, value)
        print("O: {}".format(self.array))


def _prepare_test(st_half_size, nd_half_size):
    # Test method that returns input data using even and odd numbers for the sake of readability.
    return [i for i in range(1, st_half_size * 2 + 1, 2)] + [i for i in range(2, nd_half_size * 2 + 1, 2)]


if __name__ == '__main__':
    for i in range(1, 5):
        for j in range(0, 2):
            merge = Merge(_prepare_test(i, i - j))
            merge.calculate()
            # In case of even length input it's okay for the last element not to be processed.
            for k in range(1, len(merge.debug)):
                if j != 0 and k != len(merge.debug) -1 and not merge.debug[k]:
                    print("ERROR: Something was not processed at index {}".format(k))
                    exit(1)
            print("---")
