
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1",help="first number")
    parser.add_argument("number2",help="second number")

    args = parser.parse_args()

    print(args.number1)
    print(args.number2)

    n1 = int(args.number1)
    n2 = int(args.number2)
    result = 0;

    result = n1+n2;

    print(result)
