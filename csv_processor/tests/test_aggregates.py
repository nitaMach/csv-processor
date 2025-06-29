import pytest
from csv_processor.aggregates import apply_aggregation, parse_aggregate_operation


@pytest.fixture
def sample_data():
    return [
        {"name": "iphone", "price": "999", "rating": "4.9"},
        {"name": "galaxy", "price": "1199", "rating": "4.8"},
        {"name": "redmi", "price": "199", "rating": "4.6"},
    ]


def test_parse_aggregate_operation():
    col, op = parse_aggregate_operation("price=avg")
    assert col == "price"
    assert op == "avg"


def test_apply_aggregation_avg(sample_data):
    result = apply_aggregation(sample_data, "price=avg")
    assert result[0]["avg"] == pytest.approx((999 + 1199 + 199) / 3)


def test_apply_aggregation_min(sample_data):
    result = apply_aggregation(sample_data, "price=min")
    assert result[0]["min"] == 199


def test_apply_aggregation_max(sample_data):
    result = apply_aggregation(sample_data, "price=max")
    assert result[0]["max"] == 1199


def test_apply_aggregation_invalid_column(sample_data):
    result = apply_aggregation(sample_data, "invalid=avg")
    assert result[0]["avg"] == "No numeric values found"


def test_apply_aggregation_invalid_operation(sample_data):
    with pytest.raises(ValueError):
        apply_aggregation(sample_data, "price=invalid")
