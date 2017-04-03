from test import Test

DEFAULT_TEST_PATH = 'default_test.json'


def _perform_test(test_path):
    test = Test(test_path)
    test.perform_test()


def main():
    print('Welcome to ACB-Tests!')
    _perform_test(DEFAULT_TEST_PATH)


if __name__ == "__main__":
    main()
