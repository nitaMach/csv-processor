from typing import List, Dict, Any, Tuple

AGGREGATIONS = {
    'avg': lambda values: sum(values) / len(values),
    'min': lambda values: min(values),
    'max': lambda values: max(values),
}


def parse_aggregate_operation(operation: str) -> Tuple[str, str]:
    """
        Парсит условие агрегации в формате "колонка=операция"

        Args:
            operation: Строка агрегации (например "price=min")

        Returns:
            Кортеж (колонка, операция)

        Raises:
            ValueError: Если формат некорректный
    """
    parts = operation.split('=')
    if len(parts) != 2:
        raise ValueError(f"Invalid aggregate operation: {operation}")
    return parts[0], parts[1]


def apply_aggregation(data: List[Dict[str, Any]], operation: str) -> List[Dict[str, Any]]:
    """
        Парсит условие сортировки в формате "колонка=направление"

        Args:
            data: Список словарей с данными
            operation: Строка агрегации (например "price=min")

        Returns:
            Кортеж (колонка, направление)

        Raises:
            ValueError: Если формат некорректный
    """
    column, agg_type = parse_aggregate_operation(operation)

    if agg_type not in AGGREGATIONS:
        raise ValueError(f"Unsupported aggregation type: {agg_type}")

    values = []
    for row in data:
        try:
            value = float(row[column])
            values.append(value)
        except (KeyError, ValueError):
            continue

    if not values:
        return [{agg_type: 'No numeric values found'}]

    result = AGGREGATIONS[agg_type](values)
    return [{agg_type: result}]
