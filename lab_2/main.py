import file_handler
from NIST_TESTS import NistTests


if __name__ == "__main__":
    test_c = NistTests(file_handler.read_json("sequence.json")["cpp_sequence"])
    print(test_c)
    test_c = NistTests(file_handler.read_json("sequence.json")["cpp_sequence"])
    print(test_c)