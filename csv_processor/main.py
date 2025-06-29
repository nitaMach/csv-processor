import sys
from tabulate import tabulate
from .cli import parse_args
from .processor import process_csv


def main():
    try:
        file_path, where, aggregate, order_by = parse_args()
        result = process_csv(file_path, where, aggregate, order_by)

        if aggregate:
            print(tabulate(result, headers="keys", tablefmt="pretty"))
        else:
            print(tabulate(result, headers="keys", tablefmt="pretty"))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
