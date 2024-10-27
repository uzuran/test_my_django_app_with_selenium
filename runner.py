import sys
from behave.__main__ import main as behave_main


def runner():
    # Default options
    options = ["features/", "--tags=@smoke", "--format=pretty", "--no-capture"]

    # Run Behave
    behave_main(options)


if __name__ == "__main__":
    runner()
