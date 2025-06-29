from typing import List, Dict, Any, Tuple

OPERATORS = {
    '>': lambda a, b: a > b,
    '<': lambda a, b: a < b,
    '=': lambda a, b: a == b,
}


def parse_filter_condition(condition: str) -> Tuple[str, str, str]:
    """
        Парсит условие сортировки в формате "колонка<оператор>значение"

        Args:
            condition: Строка условия (например "price>0.7")

        Returns:
            Кортеж (колонка, оператор, значение)

        Raises:
            ValueError: Если формат некорректный
    """
    for op in OPERATORS:
        if op in condition:
            parts = condition.split(op)
            if len(parts) == 2:
                return parts[0], op, parts[1]
    raise ValueError(f"Invalid filter condition: {condition}")


def apply_filter(data: List[Dict[str, Any]], condition: str) -> List[Dict[str, Any]]:
    """
        Отфильтровать данные по указанной колонке, оператору и значению

        Args:
            data: Список словарей с данными
            condition: Строка условия (например "price>0.7")

        Returns:
            Кортеж (колонка, направление)

        Raises:
            ValueError: Если формат некорректный
    """
    column, op, value = parse_filter_condition(condition)
    op_func = OPERATORS[op]

    filtered_data = []
    for row in data:
        try:
            # Попытка преобразовать в число для сравнения, если это возможно
            row_value = row[column]
            try:
                num_value = float(value)
                row_num = float(row_value)
                if op_func(row_num, num_value):
                    filtered_data.append(row)
            except ValueError:
                #  Если это не числа, то сравнивать их как строки
                if op_func(str(row_value), str(value)):
                    filtered_data.append(row)
        except KeyError:
            continue

    return filtered_data
