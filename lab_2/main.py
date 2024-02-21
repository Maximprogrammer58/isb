import file_handler
from NIST_TESTS import NistTests


if __name__ == "__main__":
    test = NistTests(file_handler.read_file("sequence/binary_sequence_Java.txt"))
    print(test.frequency_bitwise_test())