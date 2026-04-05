"""A simple greeting tool."""
import argparse


def main():
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument("name", help="Name to greet")
    parser.add_argument("--shout", action="store_true", help="UPPERCASE the greeting")
    args = parser.parse_args()
    greeting = f"Hello, {args.name}!"
    if args.shout:
        greeting = greeting.upper()
    print(greeting)


if __name__ == "__main__":
    main()
