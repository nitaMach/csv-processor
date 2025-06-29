import pytest
from csv_processor.filters import apply_filter, parse_filter_condition


@pytest.fixture
def sample_data():
    return [
        {"name": "iphone", "price": "999", "brand": "apple"},
        {"name": "galaxy", "price": "1199", "brand": "samsung"},
        {"name": "redmi", "price": "199", "brand": "xiaomi"},
    ]


def test_parse_filter_condition():
    col, op, val = parse_filter_condition("price>100")
    assert col == "price"
    assert op == ">"
    assert val == "100"


def test_apply_filter_numeric_gt(sample_data):
    filtered = apply_filter(sample_data, "price>500")
    assert len(filtered) == 2
    assert all(float(item["price"]) > 500 for item in filtered)


def test_apply_filter_numeric_lt(sample_data):
    filtered = apply_filter(sample_data, "price<500")
    assert len(filtered) == 1
    assert float(filtered[0]["price"]) < 500


def test_apply_filter_text_eq(sample_data):
    filtered = apply_filter(sample_data, "brand=apple")
    assert len(filtered) == 1
    assert filtered[0]["brand"] == "apple"


def test_apply_filter_invalid_condition(sample_data):
    with pytest.raises(ValueError):
        apply_filter(sample_data, "price!100")
