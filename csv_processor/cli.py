import argparse
from typing import Optional, Tuple


def parse_args() -> Tuple[str, Optional[str], Optional[str], Optional[str]]:
    """
        Парсит аргументы командной строки

        Returns:

            Кортеж (путь, фильтрация, агрегация, сортировка)
    """
    parser = argparse.ArgumentParser(description='Process CSV files with filtering and aggregation.')
    parser.add_argument('--file', help='Path to the CSV file')
    parser.add_argument('--where', help='Filter condition in format "column[operator]value"')
    parser.add_argument('--aggregate', help='Aggregate operation in format "column=operation"')
    parser.add_argument('--order-by', help='Sort by column in format "column=asc|desc" (e.g. "price=desc")')

    args = parser.parse_args()

    return args.file, args.where, args.aggregate, args.order_by
