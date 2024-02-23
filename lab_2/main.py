import file_handler
from NIST_TESTS import NistTests


if __name__ == "__main__":
    test_c = NistTests("1101")
    print(test_c.frequency_bitwise_test())
    print("------------------")