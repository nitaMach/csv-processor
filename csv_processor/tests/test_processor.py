import os
import pytest
from csv_processor.processor import process_csv


@pytest.fixture
def csv_file(tmp_path):
    data = """name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
poco x5 pro,xiaomi,299,4.4"""
    file_path = tmp_path / "test.csv"
    with open(file_path, 'w') as f:
        f.write(data)
    return file_path


def test_process_csv_no_operations(csv_file):
    result = process_csv(str(csv_file))
    assert len(result) == 4
    assert result[0]["name"] == "iphone 15 pro"


def test_process_csv_with_filter(csv_file):
    result = process_csv(str(csv_file), filter_condition="price>500")
    assert len(result) == 2
    assert all(float(item["price"]) > 500 for item in result)


def test_process_csv_with_aggregate(csv_file):
    result = process_csv(str(csv_file), aggregate_operation="price=avg")
    assert len(result) == 1
    assert result[0]["avg"] == pytest.approx((999 + 1199 + 199 + 299) / 4)


def test_process_csv_invalid_file():
    with pytest.raises(FileNotFoundError):
        process_csv("nonexistent.csv")
