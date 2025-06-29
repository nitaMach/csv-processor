from typing import List, Dict, Any


def parse_order_by(condition: str) -> tuple[str, str]:
    """
    Парсит условие сортировки в формате "колонка=направление"

    Args:
        condition: Строка условия (например "price=desc")

    Returns:
        Кортеж (колонка, направление)

    Raises:
        ValueError: Если формат некорректный
    """
    try:
        column, direction = condition.split('=')
        direction = direction.lower()
        if direction not in ('asc', 'desc'):
            raise ValueError("Direction must be 'asc' or 'desc'")
        if column == "":
            raise ValueError("Column name cannot be empty")
        return column.strip(), direction
    except ValueError as e:
        raise ValueError(f"Invalid order-by format: {condition}. Expected 'column=asc|desc'") from e


def apply_order_by(data: List[Dict[str, Any]], condition: str) -> List[Dict[str, Any]]:
    """
    Сортирует данные по указанной колонке

    Args:
        data: Список словарей с данными
        condition: Строка условия (например "price=desc")

    Returns:
        Отсортированный список данных
    """

    column, direction = parse_order_by(condition)

    reverse = direction == 'desc'

    def sort_key(item):
        value = item.get(column)
        # Для числовых значений сортируем как числа
        try:
            return float(value) if value is not None else 0
        except (ValueError, TypeError):
            return str(value) if value is not None else ''

    return sorted(data, key=sort_key, reverse=reverse)
