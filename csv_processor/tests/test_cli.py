import pytest
from csv_processor.cli import parse_args
from unittest.mock import patch


def test_parse_args_basic():
    test_args = ["--file", "data.csv"]
    with patch('sys.argv', ['script.py'] + test_args):
        file_path, where, aggregate, order_by = parse_args()
        assert file_path == "data.csv"
        assert where is None
        assert aggregate is None


def test_parse_args_with_filter():
    test_args = ["--file", "data.csv", "--where", "price>100"]
    with patch('sys.argv', ['script.py'] + test_args):
        file_path, where, aggregate, order_by = parse_args()
        assert where == "price>100"
        assert aggregate is None


def test_parse_args_with_aggregate():
    test_args = ["--file", "data.csv", "--aggregate", "price=avg"]
    with patch('sys.argv', ['script.py'] + test_args):
        file_path, where, aggregate, order_by = parse_args()
        assert aggregate == "price=avg"
        assert where is None


def test_parse_args_with_aggregate_and_filter():
    test_args = ["--file", "data.csv", "--where", "price>100", "--aggregate", "price=avg"]
    with patch('sys.argv', ['script.py'] + test_args):
        file_path, where, aggregate, order_by = parse_args()
        assert aggregate == "price=avg"
        assert where == "price>100"
