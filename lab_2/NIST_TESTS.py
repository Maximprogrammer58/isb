import logging
import math
import scipy

logging.basicConfig(level=logging.INFO)

pi = {0: 0.2148, 1: 0.3672, 2: 0.2305, 3: 0.1875}

class NistTests:
    BLOCK_LENGTH = 8

    def __init__(self, sequence: str) -> None:
        self.sequence = sequence
        self.length = len(sequence)

    def frequency_bitwise_test(self) -> float:
        try:
            s_sum = 0
            for bit in self.sequence:
                if int(bit) == 1:
                    s_sum += 1
                else:
                    s_sum -= 1
            s = math.fabs(s_sum) / math.sqrt(self.length)
            return math.erfc(s / math.sqrt(2))
        except ZeroDivisionError as error:
            logging.error("Division be zero")
        except Exception as error:
            logging.error(error)


    def consecutive_bits_test(self) -> float:
        try:
            percentage_units = self.sequence.count("1") / self.length
            if not (abs(percentage_units - 0.5) < (2 / math.sqrt(self.length))):
                return 0
            v_n = 0
            for i in range(self.length - 1):
                if self.sequence[i] != self.sequence[i + 1]:
                    v_n += 1
            numerator = abs(v_n - 2 * self.length * percentage_units * (1 - percentage_units))
            denominator = 2 * math.sqrt(2 * self.length) * percentage_units * (1 - percentage_units)
            return math.erfc(numerator / denominator)
        except ZeroDivisionError as error:
            logging.error("Division be zero")
        except Exception as error:
            logging.error(error)


    def longest_sequence_test(self):
        try:
            block_max_len = {}
            for step in range(0, self.length, self.BLOCK_LENGTH):
                block = self.sequence[step:step + self.BLOCK_LENGTH]
                block_length = self.length_greatest_subsequence(block, "1")
                if block_length not in block_max_len:
                    block_max_len[block_length] = 1
                else:
                    block_max_len[block_length] += 1
            v = {1: 0, 2: 0, 3: 0, 4: 0}
            for i in block_max_len:
                if i <= 1:
                    v[1] += block_max_len[i]
                elif i == 2:
                    v[2] += block_max_len[i]
                elif i == 3:
                    v[3] += block_max_len[i]
                else:
                    v[4] += block_max_len[i]
            xi_square = 0
            for i in range(4):
                xi_square += math.pow(v[i + 1] - 16 * pi[i], 2) / (16 * pi[i])
            return scipy.special.gammainc(3 / 2, xi_square / 2)
        except Exception as error:
            logging.error(error)

    @staticmethod
    def length_greatest_subsequence(sequence: str, item: str) -> int:
        max_lenght = 0
        length = 0
        for letter in sequence:
            if letter == item:
                length += 1
                max_lenght = max(max_lenght, length)
            else:
                length = 0
        return max_lenght