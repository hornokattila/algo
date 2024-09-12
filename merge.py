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
            parity_coefficient = 1 if len(self.array) % 2 == 0 else 0
            return -self._calculate_shift(len(self.array) - index - parity_coefficient)

    def _calculate_new_index(self, index):
        return index + self._calculate_shift(index)

    def _shuffle(self, index, value):
        forward_index = self._calculate_new_index(index)
        forward_value = self.array[forward_index]
        # print("index: {}, value: {} -> forward index: {} | (forward value: {})"
        #     .format(index, value, forward_index, forward_value))
        self.array[forward_index] = value
        self.debug[forward_index] = True
        if forward_value:
            self._shuffle(forward_index, forward_value)

    def run(self):
        if len(merge.array) > 2:
            value = self.array[1]
            self.array[1] = None
            self._shuffle(1, value)
        print("O: {}".format(self.array))


def _prepare_test(limit):
    # Test method that returns input data using even and odd numbers for the sake of readability.
    array = [i + 1 for i in range(limit)]
    return [*array[::2], *array[1::2]]


if __name__ == '__main__':
    for i in range(0, 12):
        merge = Merge(_prepare_test(i))
        merge.run()
        # In case of even length input it's okay for the last element not to be processed.
        for k in range(1, len(merge.debug)):
            if i % 2 == 0 and k == len(merge.debug) - 1:
                pass
            elif not merge.debug[k]:
                print("ERROR: Number was not put into place: {}".format(merge.array[k]))
        print("---")
