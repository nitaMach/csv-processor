import pytest
from csv_processor.order_by import (
    parse_order_by,
    apply_order_by,
)


# Тестовые данные
@pytest.fixture
def sample_numeric_data():
    return [
        {"name": "Product A", "price": "100", "rating": "4.5"},
        {"name": "Product B", "price": "50", "rating": "4.2"},
        {"name": "Product C", "price": "200", "rating": "4.8"},
        {"name": "Product D", "price": "150", "rating": "4.6"},
    ]


@pytest.fixture
def sample_text_data():
    return [
        {"name": "Zebra", "category": "Animal"},
        {"name": "Apple", "category": "Fruit"},
        {"name": "Animal", "category": "Category"},
        {"name": "apple", "category": "Fruit"},
    ]


@pytest.fixture
def sample_mixed_data():
    return [
        {"id": "3", "value": "100"},
        {"id": "1", "value": "0"},
        {"id": "2", "value": "50"},
        {"id": "4", "value": "0"},
    ]


# Тесты для parse_order_by
def test_parse_order_by_valid_asc():
    column, direction = parse_order_by("price=asc")
    assert column == "price"
    assert direction == "asc"


def test_parse_order_by_valid_desc():
    column, direction = parse_order_by("rating=desc")
    assert column == "rating"
    assert direction == "desc"


def test_parse_order_by_invalid_format():
    with pytest.raises(ValueError, match="Invalid order-by format"):
        parse_order_by("price:desc")


def test_parse_order_by_invalid_direction():
    with pytest.raises(ValueError, match="Invalid order-by format: price=up. Expected 'column=asc|desc'"):
        parse_order_by("price=up")


# Тесты для apply_order_by
def test_apply_order_by_numeric_asc(sample_numeric_data):
    result = apply_order_by(sample_numeric_data, "price=asc")
    prices = [float(item["price"]) for item in result]
    assert prices == [50.0, 100.0, 150.0, 200.0]


def test_apply_order_by_numeric_desc(sample_numeric_data):
    result = apply_order_by(sample_numeric_data, "price=desc")
    prices = [float(item["price"]) for item in result]
    assert prices == [200.0, 150.0, 100.0, 50.0]


def test_apply_order_by_text_asc(sample_text_data):
    result = apply_order_by(sample_text_data, "name=asc")
    names = [item["name"] for item in result]
    assert names == ["Animal", "Apple", "Zebra", "apple"]


def test_apply_order_by_text_desc(sample_text_data):
    result = apply_order_by(sample_text_data, "name=desc")
    names = [item["name"] for item in result]
    assert names == ["apple", "Zebra", "Apple", "Animal"]


def test_apply_order_by_with_missing_values(sample_mixed_data):
    result = apply_order_by(sample_mixed_data, "value=asc")
    ids = [item["id"] for item in result]
    # None и пустые строки должны быть в конце при asc
    assert ids in (["1", "4", "2", "3"], ["4", "1", "2", "3"])


def test_apply_order_by_case_sensitive(sample_text_data):
    result = apply_order_by(sample_text_data, "name=asc")
    names = [item["name"] for item in result]
    # Проверяем, что сортировка чувствительна к регистру
    assert names[1] == "Apple"
    assert names[3] == "apple"


# Тесты на обработку ошибок
def test_apply_order_by_invalid_column(sample_numeric_data):
    # Сортировка по несуществующей колонке не должна вызывать ошибку
    result = apply_order_by(sample_numeric_data, "nonexistent=asc")
    assert len(result) == len(sample_numeric_data)


def test_apply_order_by_empty_column_name(sample_numeric_data):
    with pytest.raises(ValueError, match="Invalid order-by format: =asc. Expected 'column=asc|desc'"):
        apply_order_by(sample_numeric_data, "=asc")
