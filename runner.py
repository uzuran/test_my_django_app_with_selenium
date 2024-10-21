import sys
from behave.__main__ import main as behave_main


def run_behave_tests():
    if len(sys.argv) > 1:
        # Pass command-line options, including tags
        options = sys.argv[1:]
    else:
        # Default options
        options = ["features/", "--tags", "@smoke", "--format", "pretty", "--no-capture"]

    behave_main(options)


if __name__ == "__main__":
    run_behave_tests()
