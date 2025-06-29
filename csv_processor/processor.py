import csv
from typing import List, Dict, Any, Optional
from .filters import apply_filter
from .aggregates import apply_aggregation
from .order_by import apply_order_by


def read_csv(file_path: str) -> List[Dict[str, Any]]:
    """
        Читает CSV-файл и возвращает список словарей

        Args:
            file_path: Путь до файла

        Returns:
            Список словарей с данными
    """
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def process_csv(
        file_path: str,
        filter_condition: Optional[str] = None,
        aggregate_operation: Optional[str] = None,
        order_by_condition: Optional[str] = None,

) -> List[Dict[str, Any]]:
    """
        Обработайте CSV-файл с дополнительной фильтрацией или агрегацией

        Args:
            file_path: Путь до файла
            filter_condition: Строка условия фильтрации
            aggregate_operation: Строка условия агрегации
            order_by_condition: Строка условия сортировки

        Returns:
            Список словарей с данными после обработки
    """
    data = read_csv(file_path)

    if filter_condition:
        data = apply_filter(data, filter_condition)

    if aggregate_operation:
        data = apply_aggregation(data, aggregate_operation)

    if order_by_condition:
        data = apply_order_by(data, order_by_condition)
    return data
