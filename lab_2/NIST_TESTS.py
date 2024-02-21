import math


class NistTests:
    def __init__(self, sequence: str) -> None:
        self.sequence = sequence

    def frequency_bitwise_test(self) -> float:
        s_sum = 0
        for bit in self.sequence:
            if int(bit) == 1:
                s_sum += 1
            else:
                s_sum -= 1
        s = abs(s_sum) / math.sqrt(len(self.sequence))
        return math.erfc(s/math.sqrt(2))

    def consecutive_bits_test(self):
        pass

    def longest_sequence_test(self):
        pass